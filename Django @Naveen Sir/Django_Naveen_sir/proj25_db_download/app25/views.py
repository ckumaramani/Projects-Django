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
    address= request.POST.get("address")
    salary= request.POST.get("salary")
    qs=staff(idno=idno,salary=salary,name=name,contactno=contactno,designation=designation,address=address).save()
    return redirect (request, "details.html", {"data":qs})




def downloadCSV():
    res=Httpresponse(content_type="text/css")
    res['content-Disposition']='attachment; filename="Staff details.csv"'
    write=csv.writer(res)
    qs=staff.objects.all()
    for x in qs:
        write.writerow([x.idno,x.name,x.designation,x.salary,x.address,x.contactno])
        return res
