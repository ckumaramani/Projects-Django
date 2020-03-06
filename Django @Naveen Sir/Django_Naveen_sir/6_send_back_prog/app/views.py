from django.shortcuts import render
def arjun(request):
    return render(request,"index.html")
def karjun(request):
    global fname
    fname=request.POST.get("t1")
    return render(request,"index1.html",{"fn":fname})
def mahe(request):
    lname=request.POST.get("t2")
    fullname=fname+lname
    return render(request,"index.html",{"fullname":fullname})