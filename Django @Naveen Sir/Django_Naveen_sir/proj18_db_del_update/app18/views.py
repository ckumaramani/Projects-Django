from django.shortcuts import render, redirect

# Create your views here.
from app18.models import staff


def arjun(request):
    return render(request,"index.html")


def karjun(request):
    idno=request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    staff(idno=idno,name=name,salary=salary).save()
    return render(request,"index.html",{"message":"Details Sucessfully Saved"})


def mahe(request):
    qs=staff.objects.all()
    return render(request,"details.html",{"data":qs})




def updatee(request):
    idno=request.POST.get("id")
    staff.objects.filter(idno=id).delete()
    qs=staff.objects.filter(idno=idno)
    return render(request,"details.html",{"data":qs})
