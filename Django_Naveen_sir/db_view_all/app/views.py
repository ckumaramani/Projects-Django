from django.shortcuts import render
from .models import employees

def arjun(request):
    return render(request,"index.html")

def karjun(request):
    id=request.POST.get("i")
    na= request.POST.get("n")
    sa = request.POST.get("s")

    e1=employees(idno=id, name=na, salary=sa)
    e1.save()
    return render(request,"arjun.html",{"message":"details saved"})

