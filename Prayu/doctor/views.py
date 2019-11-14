from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import DRegisterForm,DRegUpdateForm, ProfileUpdateForm
# Create your views here.

@login_required
def index(request):
	return render(request, 'doctor/homedashboard.html')

def dRegistration(request):
	if request.method == 'POST':
		form  = DRegisterForm()
		if form.is_valid():
			print(form)
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account has been created, Now you can login!')
			return redirect('Login')
	else:
		form = DRegisterForm()
	return render (request, 'doctor/dRegistration.html',{'form': form})

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = DRegUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
			request.FILES,
			instance=request.user.dprofile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your Account has been Updated')
			return redirect('profile')
	else:
		u_form = DRegUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.dprofile)

	context = {
	'u_form' : u_form,
	'p_form' : p_form
	}

	return render(request,'doctor/profile.html', context)	

@login_required
def appointment(request):
	return render(request, 'doctor/appointment.html')

@login_required
def patient(request):
	return render(request, 'doctor/patient.html')

@login_required
def payment(request):
	return render(request, 'doctor/payment.html')

@login_required
def report(request):
	return render(request, 'doctor/report.html')

@login_required
def social(request):
	return render(request, 'doctor/social.html')