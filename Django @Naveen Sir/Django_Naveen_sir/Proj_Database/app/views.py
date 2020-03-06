from django.shortcuts import render
from .models import Employee

def arjun(req):
    return render(req,"index.html")
def karjun(request):
    id=request.POST.get("id")
    na=request.POST.get("name")
    sal=request.POST.get("salary")

    e1=Employee(idno=id,name=na,salary=sal)
    e1.save()
    return render(request,"index.html",{"msg":"Employee data saved"})