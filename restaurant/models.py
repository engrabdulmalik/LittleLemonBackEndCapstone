from django.db import models

# Create your models here


class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    name = models.CharField(max_length=100)
    no_of_guests = models.IntegerField()
    booking_date = models.DateField(db_index=True)

    def __str__(self) -> str:
        return self.name
