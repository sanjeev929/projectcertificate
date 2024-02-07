from django.urls import path
from . import views

urlpatterns=[
    path('',views.registartion,name='registartion'),
    path('home/',views.home,name='home')
]