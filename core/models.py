from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MinValueValidator
from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


# Manager Class
class UserManager(BaseUserManager):

    # extra fields in case we want to extend class in a future
    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)  # helper function to lowercase email
        user.set_password(password)  # hash helper function
        user.save(using=self._db)  # in case of multiple dbs
        return user

    # create superuser helper function
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_vip = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# Model Class
class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that allows using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_vip = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Assign user manager to objects attribute
    objects = UserManager()

    USERNAME_FIELD = 'email'  # customize to email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        try:
            instrument = Instrument.objects.get(name="USD")
        except:
            instrument = Instrument()
            instrument.save()
        asset = Asset.objects.filter(owner=self).filter(instrument__name="USD").first()
        if not asset:
            asset = Asset(owner=self, instrument=instrument, quantity=100000)
            asset.save()

    # Add  AUTH_USER_MODEL to settings !!!


class Instrument(models.Model):
    """Financial instrument for customer portfolio"""
    name = models.CharField(max_length=255, unique=True)
    symbol = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.CharField(max_length=255, default="Currency")
    price = models.DecimalField(max_digits=12, decimal_places=2, default=1.0, validators=[MinValueValidator(0.01)])

    def __str__(self):
        return self.name


class Asset(models.Model):
    """Customer owned assets"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])

    def value(self):
        quantity = self.quantity
        price = self.instrument.price
        total = quantity * price
        return total

    def __str__(self):
        return f"{self.quantity} of {self.instrument}"


class BuyTransaction(models.Model):
    """Buy Asset transaction"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def value(self):
        quantity = self.quantity
        price = self.instrument.price
        total = quantity * price
        return total

    def save(self, *args, **kwargs):
        value = self.value
        cash_balance = Asset.objects.filter(owner=self.owner).filter(instrument__name="USD").first()
        cash_balance.quantity -= value
        if cash_balance.quantity < 0:
            raise ValidationError('Insufficient funds to proceed with transaction.')
        else:
            super(BuyTransaction, self).save(*args, **kwargs)
            cash_balance.save()
            existing_asset = Asset.objects.filter(owner=self.owner).filter(instrument=self.instrument).first()
            if not existing_asset:
                asset = Asset(owner=self.owner, instrument=self.instrument, quantity=self.quantity)
                asset.save()
            else:
                existing_asset.quantity += self.quantity
                existing_asset.save()

    def __str__(self):
        return f"{self.owner}: {self.quantity} of {self.instrument}"


class SellTransaction(models.Model):
    """Sell asset transaction"""
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    instrument = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)

    def value(self):
        quantity = self.quantity
        price = self.instrument.price
        total = quantity * price
        return total

    def save(self, *args, **kwargs):
        super(SellTransaction, self).save(*args, **kwargs)
        value = self.value()
        cash_balance = Asset.objects.filter(owner=self.owner).filter(instrument__name="USD").first()
        cash_balance.quantity += value
        asset = get_object_or_404(Asset, owner=self.owner, instrument=self.instrument)
        asset_balance = asset.quantity - self.quantity
        if asset_balance < 0:
            raise ValidationError('Insufficient asset quantity to proceed with transaction.')
        elif asset_balance == 0:
            asset.delete()
            cash_balance.save()
        else:
            asset.quantity -= self.quantity
            asset.save()
            cash_balance.save()

    def __str__(self):
        return f"{self.owner}: {self.quantity} of {self.instrument}"
