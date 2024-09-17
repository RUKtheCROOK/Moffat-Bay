from django.db import models
from Accounts.models import CustomUser
from Rooms.models import Room


class Reservation(models.Model):
    reservationID = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room_type_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    number_of_guests = models.SmallIntegerField()
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    reservation_status = models.CharField(max_length=20, default='Confirmed')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reservationID} - {self.user_id} - {self.room_type_id} - {self.number_of_guests} - {self.check_in_date} - {self.check_out_date} - {self.total_price} - {self.reservation_status} - {self.created_at}"