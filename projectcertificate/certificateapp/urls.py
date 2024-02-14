from django.urls import path
from . import views

urlpatterns=[
    path('',views.registartion,name='registartion'),
    path('home/',views.home,name='home'),
    path('otpverify/',views.otpverify,name='otpverify'),
    path('otpgenerate/',views.otpgenerate,name='otpgenerate'),
    path('admin/',views.admin,name='admin')
]