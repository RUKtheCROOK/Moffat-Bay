from django.contrib import admin
from .models import Reservation

# Register your models here.

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
