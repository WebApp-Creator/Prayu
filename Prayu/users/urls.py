from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="users"),
    path('medicines/', views.medicines, name="Medicines"),
    path('prodview/<int:id>', views.prodview, name="ProdView"),
    path('search/', views.search, name="Search"),
    path('doctors/', views.doctors, name="Doctors"),
    path('doctorprofile/<int:docid>', views.doctorprofile, name="DoctorProfile"),
    path('hospitals/', views.hospitals, name="Hospitals"),
    path('viewcart/', views.viewcart, name="ViewCarts"),
    path('placeorder/', views.placeorder, name="PlaceOrder"),
    path('tracker/', views.tracker, name="tracker"),
    path('contact/', views.contact, name="ContactUs"),
    path('handlerequest/', views.handlerequest, name="Handlerequest"),
]