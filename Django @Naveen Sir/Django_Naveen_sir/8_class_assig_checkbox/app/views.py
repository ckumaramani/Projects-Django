from django.shortcuts import render

def index(request):
    return render(request,"index1.html")
def arjun(request):
    lang=request.POST.getlist("cb")
    return render(request,"details.html",{"data":lang})
