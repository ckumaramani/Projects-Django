from django.shortcuts import render

# Create your views here.
def arjun(request):
    return render(request,"index.html")


def show(request):
    radio=request.POST.get("rb")
    return render(request,"index.html",{"rn":radio})