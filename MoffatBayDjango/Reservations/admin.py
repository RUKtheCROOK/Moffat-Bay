from django.contrib import admin
from .models import Reservation

# Group Names: Taylor Mommer, John Garcia, Andrew Bach, Somsak Bounchareune, Torren Davis

# This is the admin page for the Reservation model. It displays the reservation's ID, user ID, room type ID, number of guests, check in date, check out date, and created date.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['reservationID', 'user_id', 'room_type_id', 'number_of_guests', 'check_in_date', 'check_out_date', 'created_at']
    search_fields = ['user_id', 'room_type_id', 'number_of_guests', 'check_in_date', 'check_out_date', 'created_at']
    list_filter = ['room_type_id', 'number_of_guests', 'check_in_date', 'check_out_date', 'created_at']
    fieldsets = [
        ('Reservation Information', {'fields': ['user_id','room_type_id', 'number_of_guests', 'check_in_date', 'check_out_date', 'total_price', 'reservation_status']}),
        ('Date Information', {'fields': ['created_at']}),
    ]
    readonly_fields = ['created_at']
    ordering = ['created_at']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # You can customize the form here if needed
        return form
