from django.db import models

# Create your models here

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(max_length=5)
    
class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField(max_length=6)
    booking_date = models.DateTimeField(auto_now=True)