from django.shortcuts import render
from .models import Staff
from django.http import HttpResponse
import csv
def arjun(request):
    return render(request,"index.html")


def karjun(request):
    id=request.POST.get("idno")
    name=request.POST.get("name")
    sal=request.POST.get("salary")
    desig=request.POST.get("desig")
    cont=request.POST.get("contactno")
    Staff(idno=id,name=name,salary=sal,designation=desig,contactno=cont).save()
    return render(request,"index.html",{"message":"Data Saved Sucessfully"})


class Download(object):
    req=HttpResponse(content_type="text/css")
    req['content-Disposition']='attachment;filename="Arjun staff details.csv"'
    write=csv.write(req)
    qs=Staff.objects.all()
    for x in qs:
     write.writerow([x.idno,x.name,x.salary,x.designation,x.contactno])
return req