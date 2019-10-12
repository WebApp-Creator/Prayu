from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'users/index.html')

def medicines(request):
    return render(request, 'users/medicines.html')

def doctors(request):
    return render(request, 'users/doctors.html')

def hospitals(request):
    return render(request, 'users/hospitals.html')

def about(request):
    return render(request, 'users/about.html')

def contact(request):
    return render(request, 'users/contact.html')