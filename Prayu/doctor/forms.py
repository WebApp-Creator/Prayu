from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Dprofile

class DRegisterForm(UserCreationForm):
	"""docstring for DocRegisterForm"""
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class DRegForm(forms.ModelForm):
	class Meta:
		model = Dprofile
		fields = ['image','full_name']			

class DRegUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Dprofile
		fields = [
			'full_name',
			'image',
			'full_address',
			'mci_no',
			'qualification',
			'phone_no',
			'yr_expr',
			'specialities',
			'about_you'
			]