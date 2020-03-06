from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request , "loginpage.html")


def validations(request):
    uname=request.POST.get("username")
    pwd=request.POST.get("password")
    if uname== "ArjunMajeti" and pwd=="123456":
        result="Valid Details"
    else:
        result="!!!......Invalid UserName or Password.....!!!"

    return render(request ,"loginpage.html",{"res":result})