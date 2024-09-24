from django import forms
from .models import Reservation

# Group Names: Taylor Mommer, John Garcia, Andrew Bach, Somsak Bounchareune, Torren Davis

# This is the form for the Reservation model. It is used to create a new reservation.
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room_type_id', 'number_of_guests', 'check_in_date', 'check_out_date']
        widgets = {
            'room_type_id': forms.Select(attrs={'class': 'form-control'}),
            'number_of_guests': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of Guests',
                'min': 1
            }),
            'check_in_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select Check-in Date'
            }),
            'check_out_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Select Check-out Date'
            }),
        }

    # This function sets the error messages for the form.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['room_type_id'].error_messages = {
            'required': 'Please select a room type.'
        }
        self.fields['number_of_guests'].error_messages = {
            'required': 'Please enter the number of guests.'
        }
        self.fields['check_in_date'].error_messages = {
            'required': 'Please select a check-in date.'
        }
        self.fields['check_out_date'].error_messages = {
            'required': 'Please select a check-out date.'
        }