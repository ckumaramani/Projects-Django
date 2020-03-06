from django.shortcuts import render
from django.views.generic import UpdateView

from .models import Employee
# Create your views here.
def Loginpage(request):
    return render(request,"loginpage.html")


def Registerpage(request):
    return render(request, "register.html")


def saveallToDB(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    salary=request.POST.get("salary")
    contactno=request.POST.get("contactno")
    usename=request.POST.get("un")
    password=request.POST.get("up")
    image=request.FILES["image"]
    Employee(idno=idno,name=name,salary=salary,contactno=contactno,image=image,username=usename,password=password).save()
    return render(request,"register.html",{"msg":"Sucessfully Registered"})


def validations(request):
    username=request.POST.get("una")
    password=request.POST.get("upa")
    qs=Employee.objects.filter(username=username,password=password)
    if qs:
        return render(request,"Welcomepage.html")
    else:
        return render(request, "loginpage.html",{"messsage":"!!!...Invalid Details....!!!"})


def Viewall(request):
    qs=Employee.objects.all()
    return render(request,"Viewalldetails.html",{"data":qs})
