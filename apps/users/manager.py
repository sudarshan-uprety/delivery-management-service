from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

from apps.users.choices import UserRole


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', UserRole.SUPERADMIN)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if extra_fields.get('role') != UserRole.SUPERADMIN:
            raise ValueError(_('Superuser must have role=SUPERADMIN.'))

        return self.create_user(email, password, **extra_fields)

    def create_admin(self, email, password, **extra_fields):
        extra_fields.setdefault('role', UserRole.ADMIN)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)

    def create_delivery_boy(self, email, password, **extra_fields):
        extra_fields.setdefault('role', UserRole.DELIVERY_BOY)
        return self.create_user(email, password, **extra_fields)

    def create_staff(self, email, password, **extra_fields):
        extra_fields.setdefault('role', UserRole.STAFF)
        extra_fields.setdefault('is_staff', True)
        return self.create_user(email, password, **extra_fields)
