from django.db import models
from django.contrib.auth.models import User
import datetime


STATUS = ((0, "Draft"), (1, "Published"))


class No_of_guest(models.Model):
    guest = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.guest)


class OnlineBooking(models.Model):

    TIME_CHOICES = [
        ("6 PM", "6 PM"),
        ("6:30 PM", "6:30 PM"),
        ("7 PM", "7 PM"),
        ("7:30 PM", "7:30 PM"),
        ("8 PM", "8 PM"),
        ("8:30 PM", "8:30 PM"),
        ("9 PM", "9 PM"),
        ("9:30 PM", "9:30 PM"),
        ("10 PM", "10 PM"),
        ("10:30 PM", "10:30 PM"),
    ]

    OCCASSION_CHOICES = [
        ("Birthday", "Birthday"),
        ("Anniversary", "Anniversary"),
        ("Date night ", "Date night "),
        ("Business Meal", "Business Meal"),
        ("Other", "Other"),
        ]

    TABLE_CHOICES = (
        ("Family table", "Family table"),
        ("Outdoor seating", "Outdoor seating"),
        ("Table for two", "Table for two"),
        ("Table on second floor (sea view)", "Table on second floor (sea view)")
        )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='restaurant_booking'
    )
    no_of_guest = models.ForeignKey(No_of_guest, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    time = models.CharField(null=True, blank=False, choices=TIME_CHOICES, max_length=60)
    occassion = models.CharField(max_length=150, choices=OCCASSION_CHOICES, default="Birthday")
    table = models.CharField(max_length=150, choices=TABLE_CHOICES, default="Family table")
    special_request = models.TextField(max_length=300, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:

        unique_together = ["no_of_guest", "date", "time"]

    def __str__(self):
        return f'{self.date}'


class ContactDetails(models.Model):
    name = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=256, blank=True)
    address = models.CharField(max_length=256, blank=True)
    online_booking = models.ForeignKey(
        OnlineBooking, on_delete=models.CASCADE, related_name='restaurant_booking'
    )
   
    def __str__(self):
        return str(self.name)
