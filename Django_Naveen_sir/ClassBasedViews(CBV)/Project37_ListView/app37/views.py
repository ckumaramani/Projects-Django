from django.shortcuts import render

# Create your views here.
from app37.models import Arjun


def register(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    salary=request.POST.get("sal")
    desig=request.POST.get("rb")
    Arjun(idno=idno,name=name,salary=salary, designation=desig).save()
    return render(request,"index.html",{"message":"Sucessfully Registered"})


def viewall(request):
    qs=Arjun.objects.all()
    return render(request,"viewll.html",{"data":qs})