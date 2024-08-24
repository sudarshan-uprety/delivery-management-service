from django.db import models

class UserRole(models.TextChoices):
    SUPERADMIN = 'SA', 'Superadmin'
    ADMIN = 'A', 'Admin'
    DELIVERY_BOY = 'DB', 'Delivery Boy'
    STAFF = 'ST', 'Staff'
