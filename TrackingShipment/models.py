from django.db import models
from django.contrib.auth.models import User

class Shipment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'En attente de départ'),
        ('IN_TRANSIT', 'En transit'),
        ('ARRIVED', 'Arrivé à destination'),
        ('DELIVERED', 'Livré'),
    ]

    tracking_number = models.CharField(max_length=50, unique=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    departure_date = models.DateTimeField(null=True, blank=True)
    estimated_arrival = models.DateTimeField(null=True, blank=True)
    actual_arrival = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ShipmentUpdate(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='updates', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
