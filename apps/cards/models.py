from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

from auths.models import CustomUser


class Category(models.Model):
    "Cashback Categories Model."

    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Card(models.Model):
    """Bank Card Model."""

    bank_title = models.CharField(max_length=255)
    card_type = models.CharField(max_length=255)
    number = models.CharField(
        max_length=16,
        validators = [
            MaxLengthValidator(16), 
            MinLengthValidator(16)
        ]
    )
    usage_date = models.DateField()
    owner = models.ForeignKey(
        CustomUser, 
        on_delete=models.SET_NULL, 
        verbose_name='владелец карты', 
        null=True, 
        blank=True
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'карта'
        verbose_name_plural = 'карты'
