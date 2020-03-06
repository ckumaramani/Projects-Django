from django.shortcuts import render
from django.shortcuts import render
def karjun(request):
    return render(request,"index1.html")
def mahe(request):
    name=request.POST.get("t1")
    age = request.POST.get("t2")
    contact = request.POST.get("t3")
    Emailid = request.POST.get("t4")
    d1={"na":name,"ag":age,"cont":contact, "ema":Emailid}
    return render(request,"index2.html",d1)