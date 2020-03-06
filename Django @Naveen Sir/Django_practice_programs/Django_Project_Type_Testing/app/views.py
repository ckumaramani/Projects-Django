

from django.shortcuts import render

# Create your views here.
from app.models import Arjun


def show(request):
    return render(request,"index.html")


def LoginButton(request):
    un=request.POST.get("un")
    up=request.POST.get("up")
    type=request.POST.get("rd")
    qs=Arjun.objects.filter(username=up,password=up,type=rd)
    if qs:
        
        return render(request,"manager.html")
    else:
        return render(request,"index.html",{"message":"invalid details.....!!!!!!111"})
def Mlogout(request):
    return render(request,"index.html",{"mesg1":"Manager Sucessfully Logout "})


def SoftEnginlogout(request):
    return render(request,"index.html" ,{"mesg2":"Asst. Manager Sucessfully Logout "})


def Asstmanagerlogout(request):
    return render(request,"index.html" ,{"mesg4":"Software Engineer  Sucessfully Logout "})


def Register(request):
    return render(request,"Register.html")


def Registersave(request):
    un = request.POST.get("un")
    up = request.POST.get("up")
    rd = request.POST.get("rd")
    cn = request.POST.get("cn")
    idno = request.POST.get("idno")
    name=request.POST.get("name")
    Arjun(name=name,idno=idno,contactno=cn,designatoin=rd,username=un,password=up).save()
    return render(request,"index.html",{"message":"Sucessfully Registered"})


def viewall(request):
   qs= Arjun.objects.all()
   return render(request,"viewall.html",{"data":qs})


def viewDetails(request):
    pass