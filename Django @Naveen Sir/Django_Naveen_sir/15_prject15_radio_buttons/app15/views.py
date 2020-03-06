from django.shortcuts import render

def show(req):
    return render(req,"index15.html")
def arjun(request):
    item=request.POST.get("rb")
    return render(request,"index15.html",{"message":item})