from django.urls import path
from . import views

urlpatterns=[
    path('',views.registartion,name='registartion'),
    path('login/',views.login,name='login'),
    path('admin_registration/',views.admin_registration,name='admin_registration'),
    path('home/',views.home,name='home'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('otpgenerate/',views.otpgenerate,name='otpgenerate'),
    path('admin/',views.admin,name='admin')
]