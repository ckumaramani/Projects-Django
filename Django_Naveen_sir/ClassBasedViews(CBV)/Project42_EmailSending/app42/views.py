from django.shortcuts import render, redirect
from .models import Employee

# Create your views here.
def Save(request):
    idno=request.POST.get("t1")
    name=request.POST.get("t2")
    contact=request.POST.get("t3")
    email=request.POST.get("t4")
    Employee(idno=idno,name=name,contactno=contact,email=email).save()
    return redirect("main")
