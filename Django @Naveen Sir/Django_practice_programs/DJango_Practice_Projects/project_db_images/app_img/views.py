from django.shortcuts import render
from .models import A_StaffDetails
# Create your views here.
def karjun(request):
    return render(request,"index.html")


def Show(request):
    idno=request.POST.get("id")
    na=request.POST.get("name")
    de=request.POST.get("desig")
    sa=request.POST.get("sal")
    co=request.POST.get("cont")
    im=request.POST.get("img")
    A_StaffDetails(idno=idno,name=na,designation=de,salary=sa,contactno=co,image=im).save()
    return render(request,"index.html",{"mesg":"Staff Details Saved sucessfully"})


def ShowDetails(request):
    qs=A_StaffDetails.objects.all()
    return render(request,"details.html",{"data":qs})