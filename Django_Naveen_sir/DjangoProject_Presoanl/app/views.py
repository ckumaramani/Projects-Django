from django.shortcuts import render
from .models import ArjunStaff
def Login(request):
    return render(request,"index.html")


def Validation(request):
    un=request.POST.get("un")
    up=request.POST.get("up")
    qs=ArjunStaff.objects.filter(username=un, password=up)
    if qs:
        return render(request,"Welcome.html",{"message":"Welcome User"})
    else:
        return render(request,"Login.html",{"message":"Invalid Details"})


def Register(request):
    return render(request,"registration.html")


def Registered(request):
    name=request.POST.get("name")
    contact=request.POST.get("contactno")
    desig=request.POST.get("rb")
    un=request.POST.get("un")
    up=request.POST.get("up")
    ArjunStaff(name=name, contactno=contact, designation=desig, username=un, password=up).save()
    return render(request,"Login.html", {"msg":"Registration Sucessfully"})


def Homepage(request):
    return render(request,"index.html")


def Logoutbutton(request):
    return render(request,"Login.html")


def Viewallstaff(request):
    qs=ArjunStaff.objects.all()
    return render(request,"AllStaffDetails.html",{"data":qs})