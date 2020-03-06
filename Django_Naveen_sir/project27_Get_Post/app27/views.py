from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from app27.models import Login


def show(request):
    return render(request,"Login.html")


def postlogin(request):
    return render(request,"Postlogin.html")


def Pcheck(request):
    un=request.POST.get("uname")
    up=request.POST.get("upas")
    qs=Login.objects.filter(username=un, password=up)

    if qs:
        return HttpResponse ("P valid")
    else:
        return HttpResponse ("P Invalid")




def getlogin(request):
    return render(request,"getlogin.html")


def gcheck(request):
    un = request.POST.get("uname")
    up = request.POST.get("upas")
    qs = Login.objects.filter(username=un, password=up)

    if qs:
        return HttpResponse("G valid")
    else:
        return HttpResponse("G Invalid")

