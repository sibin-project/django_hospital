from django.db import models

# Create your models here.
class Departmet(models.Model):
    def_name = models.CharField(max_length=100)
    def_display_name = models.TextField()
    def_image=models.ImageField(upload_to='images/',default='img')

class doctor(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_department = models.CharField(max_length=100)
    doc_image = models.ImageField(upload_to='images/')
    doc_specialization = models.TextField()
    def __str__(self):
        return self.doc_name + "(" +self.doc_department+")"

class booking(models.Model):
    p_name=models.CharField(max_length=255)
    p_phone=models.CharField(max_length=10)
    p_email=models.EmailField()
    doc_name=models.ForeignKey(doctor,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_on=models.DateField(auto_now=True)

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