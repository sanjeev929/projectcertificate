from django.urls import path
from . import views

urlpatterns=[
    path('',views.registartion,name='registartion'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('admin_registration/',views.admin_registration,name='admin_registration'),
    path('home/',views.home,name='home'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('otpgenerate/',views.otpgenerate,name='otpgenerate'),
    path('admin/',views.admin,name='admin'),
    path('downloadcertificate/',views.downloadcertificate,name='downloadcertificate'),
    path('verify_recaptcha/',views.verify_recaptcha,name='verify_recaptcha/'),
    path('contact/',views.contact,name='contact')
]
