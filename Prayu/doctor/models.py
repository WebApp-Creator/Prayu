from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Dprofile(models.Model):
	specialities_opt = (
        ("Gynecologist", "Gynecologist"),
        ("General Physician", "General Physician"),
        ("Orthopedician", "Orthopedician"),
        ("Dietitian", "Dietitian"),
        ("Pediatrician", "Pediatrician"),
        ("Dermatologist", "Dermatologist"),
        ("Psychiatrist", "Psychiatrist"),
        ("Andrologist", "Andrologist"),
        ("Urologist", "Urologist"),
        ("General Surgeon", "General Surgeon"),
        ("Dentist", "Dentist"),
        ("Pulmonologist", "Pulmonologist"),
        ("Oncologist", "Oncologist"),
        ("Nephrologist", "Nephrologist"),
        ("Sports Medicine", "Sports Medicine"),
        ("Psychotherapist", "Psychotherapist"),
        ("Diabetologist", "Diabetologist"),
        ("Gastroenterologist", "Gastroenterologist"),
        ("Endocrinologist", "Endocrinologist"),
        ("Fertility Specialist", "Fertility Specialist"),
        ("Neurosurgeon", "Neurosurgeon"),
        ("Neurologist", "Neurologist"),
        ("Cosmetologist", "Cosmetologist")
    )

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	full_name = models.CharField(max_length=60, default="")
	mci_no = models.IntegerField(default=0)
	qualification = models.CharField(max_length=60, default="")
	full_address = models.CharField(max_length=100, default="")
	phone_no = models.IntegerField(default=0)
	yr_expr = models.IntegerField(default=0)
	specialities = models.CharField(max_length=50, choices=specialities_opt, default="please define your Specialist")
	about_you = models.TextField(max_length=30000,default="Write About Yourself...")
	image = models.ImageField(default='default_doc_pro.png', upload_to='Doctor/profile_pics')
	reg_date = models.DateTimeField(default=timezone.now)
	status = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)
