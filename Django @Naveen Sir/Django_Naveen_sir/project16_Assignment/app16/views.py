from django.shortcuts import render
from django.shortcuts import render

def arjun(req):
    return render(req,"login page.html")
def karjun(request):
    global username , password ,type, uid
    username=request.POST.get("t1")
    password=request.POST.get("t2")
    type =request.POST.get("rb")
    uid=request.POST.get("uid")
    error="wrong type"

    if username == "Ravi" and password == "ravi123" :
        if type == "Admin" :
             return render(request, "Admin.html",{"user":username})
        else:
            return render(request, "login page.html", error)
    elif username == "Ravi1" and password == "1234" :
            if type == "Employee" :
             return render(request, "employee.html",{"user":username})
            else:
                return render(request, "login page.html", error)
    elif username == "Ravi12" and password == "12345" :
            if type == "Client" :
             return render(request, "client.html",{"user":username})
            else:
                return render(request, "login page.html", error)
    else:
       return render(request, "login page.html", error)


def validate(request):
    id=request.POST.get("uid")
    #data={"username": username ,"password":  password,"type":type,"uid": uid }
    error="wrong Unique id"
    if username=="ravi1" and password=="1234" and  type== "Employee" and  uid== "0706" :
        return render(request,"uniqid.html",{"username": username ,"password":  password,"type":type,"uid": uid })
    else:
        return render(request, "employee.html", error)