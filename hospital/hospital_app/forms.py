from django import forms
from .models import booking
from .models import contact


class DateInput(forms.DateInput):
    input_type = "date"


class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = "__all__"
        widgets = {
            "booking_date": DateInput(),
            "p_name": forms.TextInput(attrs={"class": "form-control m-2 "}),
            "p_phone": forms.TextInput(attrs={"class": "form-control m-2"}),
            "p_email": forms.EmailInput(attrs={"class": "form-control m-2"}),
            
        }
        labels = {
            "p_name": "Patient Name",
            "p_phone": "Phone Number",
            "p_email": "Email Address",
            "doc_name": "Doctor Name",
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

