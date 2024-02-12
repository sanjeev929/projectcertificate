from django.urls import path
from . import views

urlpatterns=[
    path('',views.registartion,name='registartion'),
    path('home/',views.home,name='home'),
    path('verifyotp/',views.verifyotp,name='verifyotp'),
    path('otpgenerate/',views.otpgenerate,name='otpgenerate')
]