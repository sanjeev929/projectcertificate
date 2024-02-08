from django.shortcuts import render
import requests

# Create your views here.
def registartion(request):
    return render(request,'registration.html')
def home(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        data = {
            "name": name,
            "email": email,
            "phone": phone
        }
        fastapi_url = "http://192.168.143.87:8001/submit-data/"
        response = requests.post(fastapi_url, json=data)
        if response.status_code == 200:
            response_data = response.json()
            message = response_data.get("message")
            context={
                "name":name,
                "email":email
            }
            return render(request, 'home.html',context)
        else:
                context={
                "name":None,
                "email":None
            }
        return render(request, 'home.html',context)
    context={
                "name":None,
                "email":None
            }    
    return render(request, 'home.html',context)
