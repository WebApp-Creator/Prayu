from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil
from django import template

register = template.Library()
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

def prodview(request, id):
    # fetch the product using ID
    product = Product.objects.filter(product_id=id)
    # print(product); 
    return render(request, 'users/prodview.html',{'product':product[0]})

def viewcart(request):
    products = Product.objects.all()
    params = {'products':products}
    return render(request, 'users/viewcart.html', params)

def doctors(request):
    return render(request, 'users/doctors.html')

def hospitals(request):
    return render(request, 'users/hospitals.html')


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        subject=request.POST.get('subject','')
        message=request.POST.get('message','')
        contact = Contact(name=name,email=email,subject=subject,message=message)
        contact.save()
    return render(request, 'users/contact.html')
