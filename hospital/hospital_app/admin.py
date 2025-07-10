from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Departmet)
admin.site.register(doctor)
class bookingadmin(admin.ModelAdmin):
    list_display =('id','p_name','p_phone','p_email','doc_name','booking_date','booking_on')
admin.site.register(booking,bookingadmin)

class contactadmin(admin.ModelAdmin):
    list_display =('id','name','email','phone','message','contact_on')
admin.site.register(contact,contactadmin)

admin.site.register(recentNews)
admin.site.register(team)
