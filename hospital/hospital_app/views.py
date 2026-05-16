from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html',{'rn':recentNews.objects.all()})

def about(request):
    return render(request,'about.html',{'team': team.objects.all()})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('booking')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
        # Add Bootstrap classes to form fields
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
    return render(request, 'register.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('booking')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'
            
    return render(request, 'login.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')

@login_required(login_url='login')
def booking(request):
    submitted = False
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        # Pre-fill data if available from user profile (optional future enhancement)
        form = BookingForm()

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

        