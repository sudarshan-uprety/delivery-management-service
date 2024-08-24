from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.users.manager import CustomUserManager


class UserRole(models.TextChoices):
    SUPERADMIN = 'SA', 'Superadmin'
    ADMIN = 'A', 'Admin'
    DELIVERY_BOY = 'DB', 'Delivery Boy'
    STAFF = 'ST', 'Staff'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        validators=[RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')],
        blank=True,
        null=True
    )
    full_name = models.CharField(_('full name'), max_length=255, blank=True)
    role = models.CharField(max_length=2, choices=UserRole.choices)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    @property
    def is_superadmin(self):
        return self.role == UserRole.SUPERADMIN

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_delivery_boy(self):
        return self.role == UserRole.DELIVERY_BOY

    @property
    def is_regular_staff(self):
        return self.role == UserRole.STAFF

class SuperadminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.SUPERADMIN)

class AdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.ADMIN)

class DeliveryBoyManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.DELIVERY_BOY)

class StaffManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role=UserRole.STAFF)

# Add these managers to the User model
User.superadmins = SuperadminManager()
User.admins = AdminManager()
User.delivery_boys = DeliveryBoyManager()
User.staff = StaffManager()