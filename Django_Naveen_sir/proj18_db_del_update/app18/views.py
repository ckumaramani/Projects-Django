from django.shortcuts import render, redirect

# Create your views here.
from app18.models import staff


def arjun(request):
    return render(request, "index.html")


def karjun(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    staff(idno=idno, name=name, salary=salary).save()
    return render(request, "index.html", {"msg": "Details Sucessfully Saved"})


def mahe(request):
    qs = staff.objects.all()
    return render(request, "details.html", {"data": qs})


def updatee(request):
    idno = request.POST.get("id")
    qs = staff.objects.filter(idno=idno)
    return render(request, "update.html", {"data": qs})


def delete(request):
    idno = request.GET.get(id)
    staff.objects.filter(idno=idno).delete()
    return render(request, "index.html", {"message": "Sucesssfully Deleted"})


def updateemployee(request):
    idno = request.POST.get("idno")
    name = request.POST.get("name")
    salary = request.POST.get("salary")
    staff(idno=idno, name=name, salary=salary).save()
    return render(request, "index.html")
