from django.shortcuts import render
from .models import Staff
import csv
from django.http import HttpResponse
# Create your views here.
def Indexpage(request):
    return render(request,"index.html")


def Loginpageopen(request):
    return render(request,"Loginpage.html")


def Registerpageopen(request):
    return render(request,"register.html")


def openLoginpage(request):
    idno=request.POST.get("idno")
    name=request.POST.get("name")
    cn=request.POST.get("contactno")
    desig=request.POST.get("rb")
    username=request.POST.get("un")
    password=request.POST.get("up")
    Staff(idno=idno,name=name,contactno=cn,designation=desig,username=username,password=password).save()
    return render(request,"Loginpage.html",{"msg":"Registration Sucessfull"})


def gotoWelcomepage(request):
    return render(request,"welcomepage.html")


def gotologinpagefromwelpage(request):
    return render(request,"Loginpage.html")


def viewallstaffDetails(request):
    qs=Staff.objects.all()
    return render(request,"AllEmployeesdetails.html",{"data":qs})


def gotohomepage1(request):
    return render(request,"index.html")


def gotobranchesI(request):
    return render(request,"branches.html" )


def GotohomepageB(request):
    return render(request,"index.html")


def GotoaboutusI(request):
    return render(request,"Aboutus.html")


def GotocontactusI(request):
    return render(request,"Contactus.html")


def Downloadalldetails(request):
    res=HttpResponse(content_type="text\css")
    res['content-Disposition']='attachment; filename="ArjunStaffDetails.csv"'
    write=csv.writer(res)
    qs=Staff.objects.all()
    for x in qs:
        write.writerow([x.idno,x.name,x.designation,x.contactno,x.username])
    return res




