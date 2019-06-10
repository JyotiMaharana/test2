from django.shortcuts import render
from.models import RegistrationData
from.forms import RegistrationForm,LoginForm
from django.http.response import HttpResponse
def home(request):
    return render (request,'relogin.html')
def registration(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            first_name=request.POST.get("first_name",'')
            last_name=request.POST.get("last_name",'')
            user_name = request.POST.get("user_name", '')
            password1 = request.POST.get("password1", '')
            password2 = request.POST.get("password2", '')
            email = request.POST.get("email", '')
            number = request.POST.get("number", '')
            data=RegistrationData(
                first_name=first_name,
                last_name=last_name,
                user_name=user_name,
                password1=password1,
                password2=password2,
                email=email,
                number=number)
            data.save()
        form=RegistrationForm()
        return render(request,'registration.html',{'form':form})
    else:
        form=RegistrationForm()
        return render(request,'registration.html',{'form':form})
def login(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            user_name=request.POST.get('user_name','')
            password1=request.POST.get('password1','')
            user=RegistrationData.objects.filter(user_name=user_name)
            pwd=RegistrationData.objects.filter(password1=password1)
            if user and pwd:
                return HttpResponse('valid details')
            else:
                return HttpResponse('Invalid details')
    else:
        lform=LoginForm()
        return render(request,'login.html',{'form':lform})


