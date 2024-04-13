from django.db import models
from django.contrib.auth.base_user import (
    AbstractBaseUser,
    BaseUserManager,
)
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import PermissionsMixin


class CustomUserManager(BaseUserManager):
    """Custom User Manager."""

    def create_user(self, phone, password, **extra_fields):
        if not phone:
            raise ValidationError("Phone Number is required")

        user = self.model(
            phone=phone,
            password=password,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password, **extra_fields):
        user = self.create_user(phone, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom User model."""

    name = models.CharField(
        max_length=150,
        verbose_name='имя',
        blank=True,
        null=True,
    )
    surname = models.CharField(
        max_length=150,
        verbose_name='фамилия',
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=12,
        verbose_name='номер телефона',
        unique=True,
        blank=True
    )
    is_superuser = models.BooleanField(
        verbose_name='superuser',
        default=False
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='active',
        default=False
    )
    

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'