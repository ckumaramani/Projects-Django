from django.shortcuts import render

from app29.models import Staff, Feedback


def loginpage(request):
    return render(request,"loginpage.html")


def verifydetails(request):
    un=request.POST.get("un")
    up=request.POST.get("up")
    qs=Staff.objects.filter(username=un, password=up)
    if qs:
        return render(request,"welcomepage.html",{"message":"Welcome User"})
    else:
        return render(request,"loginpage.html",{"message":"!!!!....Invalid user....!!!!"})


def feedback(request):
    feb=request.POST.get("fb")
    Feedback(feedback=feb).save()
    return render(request,"welcomepage.html",{"msg":"Feedback Saved Sucessfully"})