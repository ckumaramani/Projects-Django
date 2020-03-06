from django.shortcuts import render

# Create your views here.
def arjun(request):
    return render(request,"index.html")


def lastname(request):
    global firstname
    firstname=request.POST.get("fn")
    return render(request,"details.html",{"fn":firstname})


def display(request):
    lastname=request.POST.get("ln")
    fullname=firstname+lastname
    return render(request,"index.html",{"fullname":fullname})