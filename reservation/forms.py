from django import forms
from .models import OnlineBooking, ContactDetails


class OnlineBookingForm(forms.ModelForm):
    class Meta:
        model = OnlineBooking
        fields = ['no_of_guest', 'date', 'time', 'occassion', 'table', 'special_request']
        exclude = ["user"]
        widgets = {
            'date': forms.widgets.DateInput(attrs={'type': 'date'})
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = ['name', 'email', 'phone', 'adress']