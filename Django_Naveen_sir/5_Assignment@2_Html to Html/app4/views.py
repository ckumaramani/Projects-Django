from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
def karjun(request):
    return render(request,"index1.html")
def mahe(request):
    name=request.POST.get("t1")
    age = request.POST.get("t2")
    contact = request.POST.get("t3")
    Email = request.POST.get("t4")
    d1={"na":name,"ag":age,"cont":contact, "ema":Email}
    return render(request,"index2.html",d1)

def ok(request):
    return render (request,"index3.html",{"message":"Thanks for registration"})