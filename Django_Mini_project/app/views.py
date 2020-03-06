import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Enquiry
from .models import Staff



def Indexpage(request):
    return render(request,"index.html")


def Enquirysaved(request):
    En=request.POST.get("en")
    Ed=request.POST.get("rd")
    Ec=request.POST.get("ec")
    Ea=request.POST.get("ea")
    Es=request.POST.get("es")
    Enquiry(name=En,gender=Ed,contactno=Ec,area=Ea,state=Es).save()
    return render(request,"Login.html",{"msg":"Thank You For Enquiring.....Soon We Will Contact You"})


def EnquiryI(request):
    return render(request,"Enquiryform.html")


def LoginI(request):
    return render(request,"Login.html")


def BranchesI(request):
    return render(request,"Branches.html")


def AboutusI(request):
    return render(request,"Aboutus.html")


def ContactusI(request):
    return render(request,"Contact us.html")


def indexL(request):
    return render(request,"index.html")


def RegisterPage(request):
    return render(request,"Registration Page.html")


def RegisterComplete(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    cn=request.POST.get("contactno")
    desig=request.POST.get("rb")
    salary=request.POST.get("us")
    address=request.POST.get("text")
    un=request.POST.get("un")
    up=request.POST.get("up")
    image=request.FILES["image"]
    Staff(idno=idno,name=name,designation=desig, contactno=cn,Address=address,salary=salary,username=un,password=up,image=image).save()
    return render(request, "Login.html",{"message":"Sucessfully Registered"})


def ViewAllStaff(request):
    qs=Staff.objects.all()
    return render(request,"AllStaffDetails.html",{"data":qs})


def DownloadAllDetails(request):
    res = HttpResponse(content_type="text\css")
    res['content-Disposition'] = 'attachment; filename="ArjunStaffDetails.csv"'
    write = csv.writer(res)
    qs = Staff.objects.all()
    for x in qs:
        write.writerow([x.idno, x.name, x.designation, x.contactno, x.username,x.image, x.Address ,x.salary])
    return res


def Loginvalidate(request):
    un=request.POST.get("un")
    up=request.POST.get("up")
    qs=Staff.objects.filter(username=un,password=up)
    if qs:
        return render(request,"Welcomepage.html")
    else:
        return render(request,"Login.html",{"message":"!!!!.......Invalid Details......!!!!"})