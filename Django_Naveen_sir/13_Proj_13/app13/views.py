from django.shortcuts import render

def display(request):
    return render(request, "one.html")
def arjun(request):
    kgf=request.POST.get("k")
    arya = request.POST.get("a")
    return render(request, "two.html", {"data":(kgf, arya)})
