from django.db import models

# Create your models here.

# Group Names: Taylor Mommer, John Garcia, Andrew Bach, Somsak Bounchareune, Torren Davis

# This is the model for the Room table. It contains all information about the rooms that are available for booking.
class Room(models.Model):
    roomTypeID = models.AutoField(primary_key=True)
    room_type_name = models.CharField(max_length=50)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    max_occupancy = models.IntegerField()
    room_description = models.CharField(max_length=500) #May keep or remove


    def __str__(self):
        return self.room_type_name + ' - $' + str(self.base_price) + ' - Max Guests:' + str(self.max_occupancy)