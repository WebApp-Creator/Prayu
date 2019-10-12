from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="users"),
    path('medicines/', views.medicines, name="Medicines"),
    path('doctors/', views.doctors, name="Doctors"),
    path('hospitals/', views.hospitals, name="Hospitals"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),

]