from django.db import models

# Create your models here.

class Room(models.Model):
    roomTypeID = models.AutoField(primary_key=True)
    room_type_name = models.CharField(max_length=50)
    base_price = models.DecimalField(max_digits=6, decimal_places=2)
    max_occupancy = models.IntegerField()
    room_description = models.CharField(max_length=500) #May keep or remove


    def __str__(self):
        return self.room_type_name + ' - $' + str(self.base_price) + ' - Max Guests:' + str(self.max_occupancy)