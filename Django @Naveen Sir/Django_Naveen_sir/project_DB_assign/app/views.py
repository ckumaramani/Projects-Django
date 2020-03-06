from django.shortcuts import render
from .models import Employee
def arjun(request):
    return render(request,"details.html")
def karjun(request):
    i=request.POST.get("id")
    n=request.POST.get("name")
    a=request.POST.get("age")
    s=request.POST.get("salary")
    d=request.POST.get("desig")
    sh=request.POST.get("rd")
    lo=request.POST.get("cb1,cb2,cb3,cb4")
    if lo= cb1:
        s= s-12500.00
    elif:
        lo= cb1, cb2
        s=s-12500.00-15000.00
    elif:
        lo= cb1 , cb2 , cb3
        s=s-12500.00-15000.00-7500.00
    else:
        s





    e1=Employee(idno=i,name=n,age=a,netsalary=s,designation={"d"},shift={"sh"},loans=lo)
    e1.save()

    return render(request,"details.html",{"message":"Employee Detail`s Saved Sucessfully"})
