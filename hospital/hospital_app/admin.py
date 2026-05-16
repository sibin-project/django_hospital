from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Department)
admin.site.register(Doctor)
class bookingadmin(admin.ModelAdmin):
    list_display =('id','patient_name','patient_phone','patient_email','doctor_name','booking_date','booked_on')
admin.site.register(Booking,bookingadmin)

class contactadmin(admin.ModelAdmin):
    list_display =('id','name','email','phone','message','contact_on')
admin.site.register(contact,contactadmin)

admin.site.register(recentNews)
admin.site.register(team)
