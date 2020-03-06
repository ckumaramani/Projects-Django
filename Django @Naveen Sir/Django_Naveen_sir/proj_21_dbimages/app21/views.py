from django.shortcuts import render

# Create your views here.
from app21.models import employee


def arjun(request):
    return render(request,"index.html")


def karjun(request):
    idno=request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    image = request.FILES["image"]
    employee(idno=idno, name=name, salary=salary,image=image).save()
    return render(request,"index.html",{"message":"saved"})


def mahe(request):
    qs=employee.objects.all()

    return render(request,"details.html",{"data":qs})