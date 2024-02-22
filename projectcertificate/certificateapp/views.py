from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse
from django.http import JsonResponse
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))  # Connecting to a public IP address to get the local IP
ip_address = s.getsockname()[0]
s.close()
ip=ip_address
# Create your views here.
def registartion(request):
    return render(request,'registration.html')

def verify_recaptcha(request):
    recaptcha_response = request.POST.get("recaptchaResponse")
    secret_key = "6Le9jncpAAAAAPYWAaCJCwjtORLoZFH-cJ6KY1aX"
    try:
    # Send a GET request to Google's reCAPTCHA verification endpoint
        response = requests.post(
            "https://www.google.com/recaptcha/api/siteverify",
            data={"secret": secret_key, "response": recaptcha_response}
        )
        data = response.json()
    except Exception as e:
        pass   
    # Return JSON response based on reCAPTCHA verification result
    return JsonResponse(data)

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
            error = response_data.get("error")
            if error:
                context={
                    "emailcheckexist":"Email is already register!!!!"
                }
                return render(request, 'registration.html',context)
            else:
                context={
                    "name":name,
                    "email":email
                }
            return render(request, 'home.html',context)
        else:
            return render(request, 'registration.html')
    return render(request, 'registration.html')

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
        if response.status_code == 200:
            response_data = response.json()
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
        statechange=request.POST.get("statechange")
        data = {
            "email": email,
            "status":statechange
        }
        fastapi_url = f"http://{ip}:8001/adminchange/"
        response = requests.post(fastapi_url, json=data)
        fastapi_url = f"http://{ip}:8001/getall/"
        response = requests.get(fastapi_url)
        if response.status_code == 200:
            response_data = response.json()
            # print(response_data)
            # alldata=response_data["users"]
            names = [user['name'] for user in response_data]
            emails = [user['email'] for user in response_data]
            phones = [user['phone'] for user in response_data]
            states = [user['status'] for user in response_data]
            userdata=sorted(zip(names,emails,phones,states),key=lambda x: x[0])
            conetxt={
                "userdata":userdata
            }
            return render(request,"admin.html",conetxt)
    else:
        fastapi_url = f"http://{ip}:8001/getall/"
        response = requests.get(fastapi_url)
        if response.status_code == 200:
            response_data = response.json()
            # print(response_data)
            # alldata=response_data["users"]
            names = [user['name'] for user in response_data]
            emails = [user['email'] for user in response_data]
            phones = [user['phone'] for user in response_data]
            states = [user['status'] for user in response_data]
        userdata=sorted(zip(names,emails,phones,states),key=lambda x: x[0])
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
        if response.status_code == 200:
            response_data = response.json()
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
        if response.status_code == 200:
            response_data = response.json()
            state = response_data.get("state")
            error = response_data.get("error")
            if state:
                return render(request, 'login.html')
            else:
                 return render(request,'admin_registration.html',{"error":error}) 
    else:
        return render(request, 'admin_registration.html')

def downloadcertificate(request):
    if request.method == "POST":
        email = request.POST.get("email")
        data = {
            "email": email
        }
        fastapi_url = f"http://{ip}:8001/downloadcertificate/"
        response = requests.post(fastapi_url, json=data)
        if response.status_code == 200:
            certificate_data = response.content
            # Set the response content type to 'application/pdf'
            response = HttpResponse(certificate_data, content_type='application/pdf')
            
            # Remove the .crdownload extension from the filename, if present
            filename = "certificate.pdf"
            if filename.endswith('.crdownload'):
                filename = filename[:-len('.crdownload')]

            # Set the Content-Disposition header to force download and provide the modified filename
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

            # Add additional security headers
            response['X-Content-Type-Options'] = 'nosniff'
            response['X-Frame-Options'] = 'deny'
            response['Content-Security-Policy'] = "default-src 'self'"

            return response
        else:
            return render(request, 'admin_registration.html', {"error": f"Server returned status code {response.status_code}."})
    else:
        return render(request, 'admin_registration.html')
       