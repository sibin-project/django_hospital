from django.db import models

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_description = models.TextField()
    department_image=models.ImageField(upload_to='images/',default='img')

class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_department = models.CharField(max_length=100)
    doctor_image = models.ImageField(upload_to='images/')
    doctor_specialization = models.TextField()
    def __str__(self):
        return self.doctor_name + "(" +self.doctor_department+")"

class Booking(models.Model):
    patient_name=models.CharField(max_length=255)
    patient_phone=models.CharField(max_length=10)
    patient_email=models.EmailField()
    doctor_name=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

class contact(models.Model):
        name=models.CharField(max_length=255)
        email=models.EmailField()
        phone=models.CharField(max_length=10)
        message=models.TextField()
        contact_on=models.DateField(auto_now=True)
        def __str__(self):
            return self.name + "(" +self.email+")" 
class  recentNews(models.Model):
     heading=models.CharField(max_length=100)
     news=models.CharField(max_length=200)
     img=models.ImageField( upload_to='images/' )
    
class team(models.Model):
    img=models.ImageField(upload_to="images/")
    name=models.CharField( max_length=100)
    position=models.CharField(max_length=150)