from django.shortcuts import render

def show(req):
    return render (req,"index.html")
def display(request):
    item  =request.POST.get("token")
    if item == "select":
        return render(request, "index.html", {"mmessage":"plesae select one item"})
    else:
      return render(request,"index.html",{"message":item })