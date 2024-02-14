from django.shortcuts import render,redirect
import requests

ip="192.168.21.87"
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
        fastapi_url = f"http://{ip}:8001/submit-data/"
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

def otpverify(request):
    if request.method == "POST":
        email = request.POST.get("mail")
        otp = request.POST.get("otp")
        data = {
            "email": email,
            "otp":otp
        }
        fastapi_url = f"http://{ip}:8001/otpverify/"
        response = requests.post(fastapi_url, json=data)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            otp_status = response_data.get("otp status")
            name = response_data.get("name")
            if otp_status:
                context={
                    "name":name,
                    "email":email,
                }
                return render(request, 'download.html',context)
            else:
                 context={
                    "name":name,
                    "email":email,
                    "error":"OTP is not valid"
                }
            return render(request,'home.html',context)
        
    return render(request, 'home.html')
def otpgenerate(request):
    if request.method == "POST":
        email = request.POST.get("email")
        data = {
            "email": email
        }
        fastapi_url = f"http://{ip}:8001/otpgenerate/"
        response = requests.post(fastapi_url, json=data)
        print(response)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            name = response_data.get("name")
            error = response_data.get("error")
            if name != None:
                context={
                    "name":name,
                    "email":email,
                }
                return render(request, 'home.html',context)
            else:
                 return render(request,'registration.html',{"error":error})
        else:
                context={
                "name":None,
                "email":None
            }
        return render(request, 'home.html')
    return render(request, 'home.html')

def admin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        data = {
            "email": email
        }
        fastapi_url = f"http://{ip}:8001/adminchnage/"
        response = requests.post(fastapi_url, json=data)
        fastapi_url = f"http://{ip}:8001/getall/"
        response = requests.get(fastapi_url)

        return render(request, 'admin.html')
    else:
        fastapi_url = f"http://{ip}:8001/getall/"
        response = requests.get(fastapi_url)
        print(response)
        if response.status_code == 200:
            response_data = response.json()
            alldata=response_data["users"]
            names = [user['name'] for user in alldata]
            emails = [user['email'] for user in alldata]
            phones = [user['phone'] for user in alldata]
            states = [user['status'] for user in alldata]
        userdata=zip(names,emails,phones,states)
        conetxt={
            "userdata":userdata
        }
        return render(request,"admin.html",conetxt)
     
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {
            "email": email,
            "password":password
        }
        fastapi_url = f"http://{ip}:8001/login/"
        response = requests.post(fastapi_url, json=data)
        print(response)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            state = response_data.get("state")
            error = response_data.get("error")
            if state:
                context={
                    "name":state,
                    "email":email,
                }
                return redirect(admin)
            else:
                 return render(request,'login.html',{"error":error}) 
    else:
        return render(request, 'login.html')
        
def admin_registration(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        data = {
            "name":name,
            "email": email,
            "password":password
        }
        fastapi_url = f"http://{ip}:8001/admin_registration/"
        response = requests.post(fastapi_url, json=data)
        print(response)
        if response.status_code == 200:
            response_data = response.json()
            print(response_data)
            state = response_data.get("state")
            error = response_data.get("error")
            if state:
                return render(request, 'login.html')
            else:
                 return render(request,'admin_registration.html',{"error":error}) 
    else:
        return render(request, 'admin_registration.html')