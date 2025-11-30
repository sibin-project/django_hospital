from django import forms
from .models import Booking
from .models import contact


class DateInput(forms.DateInput):
    input_type = "date"


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            "booking_date": DateInput(),
            "patient_name": forms.TextInput(attrs={"class": "form-control m-2 "}),
            "patient_phone": forms.TextInput(attrs={"class": "form-control m-2"}),
            "patient_email": forms.EmailInput(attrs={"class": "form-control m-2"}),
            
        }
        labels = {
            "patient_name": "Patient Name",
            "patient_phone": "Phone Number",
            "patient_email": "Email Address",
            "doctor_name": "Doctor Name",
            "booking_date": "Booking Date",
        }
class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control m-2 "}),
            "email": forms.EmailInput(attrs={"class": "form-control m-2"}),
            "phone": forms.TextInput(attrs={"class": "form-control m-2"}),
            "message": forms.Textarea(attrs={"class": "form-control m-2"}),
        }
        labels = {
            "name": "Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "message": "Message",
        }

