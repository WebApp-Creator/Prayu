from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.

def index(request):
    # products = Product.objects.all()
    # print(products)
    return render(request, 'users/index.html')

def medicines(request):
    allprods = []
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod, range(1, nSlides), nSlides])
    params = {'allprods': allprods}
    # print(params)
    return render(request, 'users/medicines.html', params)

def doctors(request):
    return render(request, 'users/doctors.html')

def hospitals(request):
    return render(request, 'users/hospitals.html')

def about(request):
    return render(request, 'users/about.html')

def contact(request):
    return render(request, 'users/contact.html')