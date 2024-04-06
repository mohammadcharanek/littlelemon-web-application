from django.db import models

class Booking(models.Model):
    # Your Booking model fields here
    customer_name = models.CharField(max_length=100)
    booking_date = models.DateField()
    # Add more fields as needed

    def __str__(self):
        return self.customer_name
