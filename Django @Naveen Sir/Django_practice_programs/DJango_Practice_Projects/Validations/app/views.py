from django.shortcuts import render
from django.shortcuts import render
def arjun(request):
    return render (request,"index.html")
def karjun(request):

    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "Ravi" and   password == "ravi123":
        result= "valid"
    else:
        result="!!!...invalid User....!!!"
    return  render(request,"index.html",{"res":result})