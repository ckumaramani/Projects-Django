from django.shortcuts import render
from .models import Staff
# Create your views here.
def loginpage(request):
    return render(request,"loginpage.html")


def validation(request):
    un=request.POST.get("username")
    up=request.POST.get("password")
    qs=Staff.objects.filter(username=un, password=up)
    if qs:
        return render(request,"homepage.html")
    else:
        return render(request,"loginpage.html",{"message":"Invalid User Details"})


def registerpage(request):
    return render(request,"register.html")


def saved(request):
    name = request.POST.get("name")
    contactno = request.POST.get("contactno")
    un = request.POST.get("username")
    up = request.POST.get("password")
    Staff(name=name, contactno=contactno, username=up, password=up).save()
    return render(request,"loginpage.html",{"msg":"Sucessfully Registered"})