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










