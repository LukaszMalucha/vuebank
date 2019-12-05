from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from core.models import Instrument, Asset, BuyTransaction, SellTransaction


# Slug creators for models for better navigation

@receiver(pre_save, sender=Instrument)
def add_slug_to_instrument(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.name)
        random_string = generate_random_string()
        instance.slug = "i-" + slug + "-" + random_string


@receiver(pre_save, sender=Asset)
def add_slug_to_asset(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.instrument.name)
        random_string = generate_random_string()
        instance.slug = "a-" + slug + "-" + random_string


@receiver(pre_save, sender=BuyTransaction)
def add_slug_to_buy_transaction(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.instrument.name)
        random_string = generate_random_string()
        instance.slug = "buy-" + slug + "-" + random_string


@receiver(pre_save, sender=SellTransaction)
def add_slug_to_sell_transaction(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.instrument.name)
        random_string = generate_random_string()
        instance.slug = "sell-" + slug + "-" + random_string
