from django.shortcuts import render
from django.http import HttpResponse
def show(request):
    return render(request,"index.html")

def display(request):
    a=request.POST.get("t1")
    b=request.POST.get("t2")
    c=request.POST.get("t3")
    return HttpResponse("Thanks")
