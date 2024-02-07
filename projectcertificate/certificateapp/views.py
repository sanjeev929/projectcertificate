from django.shortcuts import render

# Create your views here.
def registartion(request):
    return render(request,'registration.html')
def home(request):
    name = request.POST["name"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    print(name,email,phone)
    context={
        "name":name,
        "email":email
    }
    return render(request,'home.html',context)
