from django.shortcuts import render
from .models import Employees
# Create your views here.
def showimages(request):
    return render(request,"index.html")


def savedetails(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    salary=request.POST.get("salary")
    contactno=request.POST.get("cn")
    image=request.FILES["image"]
    Employees(idno=idno, name=name, salary=salary, contactno=contactno,image=image).save()
    return render(request,"index.html",{"message":"Data Inserted Sucessfully"})


def viewalldetails(request):
    qs=Employees.objects.all()
    return render(request,"ViewwallDetails.html",{"data":qs})