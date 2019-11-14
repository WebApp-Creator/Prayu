from django.urls import path
from . import views as doc_user
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', doc_user.index, name="doctor"),
    path('appointment/', doc_user.appointment, name="appointment"),
    path('patient/', doc_user.patient, name="patient"),
    path('payment/', doc_user.payment, name="payment"),
    path('report/', doc_user.report, name="report"),
    path('social/', doc_user.social, name="social"),
    path('dRegistration/',doc_user.dRegistration, name="dRegistration"),
    path('profile/',doc_user.profile, name="profile"),
    path('login/',auth_views.LoginView.as_view(template_name='doctor/login.html'), name='Login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='doctor/logout.html'), name='Logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='doctor/password_reset.html'), name='Password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='doctor/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='doctor/password_reset_confirm.html'), name='password_reset_confirm'),
]