import uuid

from django.db import models

from apps.common.models import BaseModel


class Order(BaseModel):
    PAYMENT_METHOD_CHOICES = [
        ('ONLINE', 'Online'),
        ('COD', 'Cash on Delivery'),
    ]
    DELIVERY_STATUS_CHOICES = [
        ('PRODUCT_DISPATCHED', 'Product Dispatched'),
        ('PRODUCT_DELIVERED', 'Product Delivered'),
        ('ON_ROUTE', 'On Route'),
        ('UNKNOWN', 'Unknown'),
        ('CANCELLED', 'Cancelled'),
        ('RECEIVER_FAILED', 'Receiver Failed'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    order_id = models.CharField(max_length=255, unique=True)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    payment_status = models.BooleanField(default=False)
    amount_to_receive = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    payment_method = models.CharField(max_length=255, choices=PAYMENT_METHOD_CHOICES)
    delivery_status = models.CharField(max_length=255, choices=DELIVERY_STATUS_CHOICES, null=True, blank=True)

    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=15, null=True, blank=True)
    customer_secondary_phone = models.CharField(max_length=15, null=True, blank=True)
    customer_email = models.EmailField(null=True, blank=True)

    delivery_address = models.TextField()
    delivery_city = models.CharField(max_length=100)
    delivery_state = models.CharField(max_length=100)
    delivery_zip_code = models.CharField(max_length=20)

    expected_delivery_date = models.DateTimeField(null=True, blank=True)
    actual_delivery_date = models.DateTimeField(null=True, blank=True)

    delivery_person = models.CharField(max_length=255, null=True, blank=True)
    delivery_person_contact = models.CharField(max_length=15, null=True, blank=True)

    delivery_instructions = models.TextField(null=True, blank=True)
    order_notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.order_id
