from django.shortcuts import render
from .models import Sessions
from .models import Feedback
# Create your views here.
def Loginpage(request):
    return render(request,"login.html")


def WelcomePage(request):
    un=request.POST.get("un")
    up=request.POST.get("up")
    qs=Sessions.objects.filter(username=un, password=up)
    if qs:
        return render(request,"welcomepage.html",{"msg":"Welcome User"})
    else:
        return render(request,"login.html",{"msg":"Invalid user"})


def SubmitMsg(request):
    fb=request.POST.get("fb")
    Feedback(feedback=fb).save()
    return render(request,"welcomepage.html",{"message":"Feedback Saved Sucessfully"})