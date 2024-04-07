from django.db import models

# Create your models here.
# In your Django app's models.py file


from django.contrib.auth.models import User

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class TableBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    booking_time = models.DateTimeField()
    guests_count = models.IntegerField()

    def __str__(self):
        return f"Booking for {self.user.username} at Table {self.table_number}"

# You might have more models like UserProfile for additional user information, etc.

