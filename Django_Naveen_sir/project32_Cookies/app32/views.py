from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,"index.html")


def setcookie(request):
    res=HttpResponse("Cookie is saved")
    res.set_cookie("name","Arjun")
    return res
def getcookie(request):
    req=request.COOKIES["name"]
    response=HttpResponse("The Cookie Is"+req)
    return req