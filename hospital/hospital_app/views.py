from django.shortcuts import render
from django.http import JsonResponse
from.models import *

from.forms import *


# Create your views here.
def index(request):
    
    return render(request,'index.html',{'rn':recentNews.objects.all()})
def about(request):

    return render(request,'about.html',{'team': team.objects.all()})
def booking(request):
  
    
    submitted = False
    form = BookingForm()
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True

    return render(request, 'booking.html', {'form': form, 'submitted': submitted})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'message': 'Form submitted'})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'contact_form': form})
def doctors(request):
    return render(request, 'doctors.html', {'doc': Doctor.objects.all()})

def department(request):
    dict_dept={
        'dept':Department.objects.all()
    }
    return render(request,'department.html',dict_dept)

        