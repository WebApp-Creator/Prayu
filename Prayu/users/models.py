from django.db import models

# Create your models here.

class Product(models.Model):

    category_opt = (
        ("Ayurveda", "Ayurveda"),
        ("Vitamins & Supplements", "Vitamins & Supplements"),
        ("Homeopathy", "Homeopathy"),
        ("Protein Supplements","Protein Supplements"),
        ("Elderly Care","Elderly Care"),
        ("Sexual Wellness","Sexual Wellness"),
        ("Health Food & Drinks","Health Food & Drinks"),
        ("Healthcare Devices","Healthcare Devices"),
        ("Other's", "Other's")
    )
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=category_opt)
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="PriminationShop/images", default="")

    def __str__(self):
        return self.product_name