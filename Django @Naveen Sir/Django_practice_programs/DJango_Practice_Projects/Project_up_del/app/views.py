from django.shortcuts import render
from .models import Staff
# Create your views here.
def show(request):
    return render(request, "index.html")


def Register(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    salary=request.POST.get("salary")
    cn=request.POST.get("cn")
    Staff(idno=idno,name=name, salary=salary,contactno=cn).save()
    return render(request,"index.html",{"msg":"Sucessfully Registered"})


def viewall(request):
    qs=Staff.objects.all()
    return render(request,"Viewalldetails.html",{"data":qs})


def updatedetails(request):
    idno=request.POST.get("idno")
    qs=Staff.objects.filter(idno=idno)
    return render(request,"update.html",{"data":qs})


def updatee(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    cn = request.POST.get("cn")
    Staff(idno=idno, name=name, salary=salary, contactno=cn).save()
    return render(request, "index.html",{"message":"Sucessfully Updated"})


def Delete(request):
    idno=request.GET.get("idno")
    Staff.objects.filter(idno=idno).delete()
    return render(request,"update.html")