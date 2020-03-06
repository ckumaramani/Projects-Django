from django.shortcuts import render, redirect
from app25.models import staff
from django.http import HttpResponse
import csv

def arjun(request):
    return render(request,"index.html")


def karjun(request):
    idno=request.POST.get("idno")
    name = request.POST.get("name")
    contactno = request.POST.get("contactno")
    designation= request.POST.get("designation")

    salary= request.POST.get("salary")
    staff(idno=idno,salary=salary,name=name,contactno=contactno,designation=designation).save()
    return render (request,"index.html",{"message":"Data saved Sucessfully"})


def viewDetails(request):
    qs=staff.objects.all()

    return render(request,"details.html",{"data":qs})


def downloadCSV(request):
    res=HttpResponse(content_type="text/css")
    res['content-Disposition']='attachment; filename="Staff details.csv"'
    write=csv.writer(res)
    qs=staff.objects.all()
    for x in qs:
        write.writerow([x.idno,x.name,x.designation,x.salary,x.contactno])
    return res


