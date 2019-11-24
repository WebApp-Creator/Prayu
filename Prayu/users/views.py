from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
from django import template
from doctor.models import Dprofile
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum

MERCHANT_KEY = '6T0UvRWlj2Gw8rid';

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

def searchMatch(query,item):
    ''' Return true only if query matches the item '''
    if query in item.company.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allprods = []
    #print(query)
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nSlides), nSlides])
    params = {'allprods': allprods, 'msg': ""}
    if len(allprods) == 0 or len(query)<3:
        params = {'msg': "Please make sure to relevent search query"}
    print(params)
    return render(request, 'users/medicines.html', params)

def prodview(request, id):
    # fetch the product using ID
    product = Product.objects.filter(product_id=id)
    print(product); 
    return render(request, 'users/prodview.html',{'product':product[0]})

def viewcart(request):
    products = Product.objects.all()
    params = {'products':products}
    return render(request, 'users/viewcart.html', params)

def tracker(request):
    if request.method=="POST":
        order_id = request.POST.get('order_id','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=order_id, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates =[]
                for item in update:
                    updates.append({'text': item.update_desc, 'time':item.timestamp})
                    response = json.dumps(updates)
                return HttpResponse(response)
            else:
                pass
        except Exception as e:
            return HttpResponse("hee")
    return render(request, 'users/tracker.html')

def doctors(request):
	dprofile = Dprofile.objects.all()
	print(dprofile)
	return render(request, 'users/doctors.html',{'dprofile':dprofile})

def doctorprofile(request, docid):
	dprofile = Dprofile.objects.filter(id=docid)
	print(dprofile)
	return render(request, 'users/doctorprofile.html',{'dprofile':dprofile})

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

def placeorder(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson', '')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        email=request.POST.get('email','')
        address1=request.POST.get('address1','') 
        address2=request.POST.get('address2','') 
        state=request.POST.get('state','')
        city=request.POST.get('city','')
        pin=request.POST.get('pin','')
        mobile=request.POST.get('mobile','')
        order = Order(items_json=items_json,name=name,amount=amount,email=email,address1=address1,address2=address2,state=state,city=city,pin=pin,mobile=mobile)
        order.save()
        update = OrderUpdate(order_id=order.order_id,update_desc = "The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        print(id)
        # return render(request, 'users/placeorder.html',{'thank':thank, 'id':id})
        # Request paytm to transfer the amount to your account after payment by users
        param_dict = {
            'MID':'WXbBMS05969295798845',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/users/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'users/paytm.html',{'param_dict':param_dict})

    return render(request, 'users/placeorder.html')


@csrf_exempt
def handlerequest(request):
    # PayTm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
  
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('Order has been placed Sussessful')
        else:
            print('Order was not Sussessful because'+ response_dict['RESPMSG'])
    return render(request,'users/paymentstatus.html',{'response': response_dict})