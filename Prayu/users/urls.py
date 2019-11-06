from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="users"),
    path('medicines/', views.medicines, name="Medicines"),
    path('prodview/<int:id>', views.prodview, name="ProdView"),
    path('search/', views.search, name="Search"),
    path('doctors/', views.doctors, name="Doctors"),
    path('hospitals/', views.hospitals, name="Hospitals"),
    path('viewcart/', views.viewcart, name="ViewCarts"),
    path('contact/', views.contact, name="ContactUs"),

]