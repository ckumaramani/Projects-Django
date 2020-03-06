from django.shortcuts import render, redirect
from .models import Login
from .models import FeedBack

def login(request):
    return render(request,"loginpage.html")


def Welcomepage(request):
    name = request.session["name"]
    if name:
        return render(request, "welcomepage.html", {"message": "Welcome User"})
    else:

        un=request.POST.get("un")
        up=request.POST.get("up")

    qs=Login.objects.filter(username=un, password=up)
    if qs:
        request.session["name"] = un  # Writing username to Sessions table
        return render(request,"Welcomepage.html",{"message":"Welcome user"})
    else:
        return render(request,"loginpage.html",{"message":"invalid user Details"})




def feedback(request):
    fb=request.POST.get("fb")
    name = request.session["name"]
    FeedBack(useername=name , fb=fb).save()
    return redirect("welcomepage/")