from django.db import models
from doctor.models import Dprofile

# Create your models here.

class Product(models.Model):
    category_opt = (
        ("Ayurveda", "Ayurveda"),
        ("Vitamins & Supplements", "Vitamins & Supplements"),
        ("Homeopathy", "Homeopathy"),
        ("Protein Supplements", "Protein Supplements"),
        ("Elderly Care", "Elderly Care"),
        ("Sexual Wellness", "Sexual Wellness"),
        ("Health Food & Drinks", "Health Food & Drinks"),
        ("Healthcare Devices", "Healthcare Devices"),
        ("Other's", "Other's")
    )
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=category_opt)
    company = models.CharField(max_length=50, default="")
    maxretailprice = models.IntegerField(default=0)
    sallingprice = models.IntegerField(default=0)
    desc = models.TextField(max_length=2000, default="null")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="users/images", default="")

    def __str__(self):
        return self.product_name
    
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=60, default="")
    subject = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0  )
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    address1 = models.CharField(max_length=100, default="") 
    address2 = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    pin = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=100, default="")

    def __str__(self):
        return f'Order Id: {self.order_id}'

class OrderUpdate(models.Model):
    upload_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default=0)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[:7] + "..."