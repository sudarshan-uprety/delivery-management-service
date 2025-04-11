from django.db import models


class UserRole(models.TextChoices):
    SUPERADMIN = 'SA', 'Super Admin'
    ADMIN = 'A', 'Admin'
    DELIVERY_BOY = 'DB', 'Delivery Boy'
    STAFF = 'ST', 'Staff'

    # choices = [
    #     (SUPERADMIN, 'Super Admin'),
    #     (ADMIN, 'Admin'),
    #     (DELIVERY_BOY, 'Delivery Boy'),
    #     (STAFF, 'Staff'),
    # ]
