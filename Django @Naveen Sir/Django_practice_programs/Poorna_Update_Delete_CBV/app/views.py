from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView,DetailView,ListView,UpdateView,DeleteView

from app.models import Employee


def Loginpage(request):
    return  render( request,"loginpage.html")


class Register(CreateView):
    template_name = "register.html"
    model = Employee
    fields = ['idno','name','salary','contactno','username','password']
    success_url ="/login/"


def validations(request):
    username=request.POST.get("una")
    password=request.POST.get("upa")
    qs=Employee.objects.filter(username=username,password=password)
    if qs:
        return render(request,"welcomepage.html")
    else:
        return render(request,"loginpage.html",{"msg":"Invalid Details"})


class Listview(ListView):
    template_name = "viewall.html"
    model = Employee


def Viewall(request):
    qs=Employee.objects.all()
    return render(request,"viewall.html",{"data":qs})


class Update(UpdateView):
    template_name = "update.html"
    model = Employee
    fields = ['idno', 'name', 'salary', 'contactno', 'username',]
    success_url = "/viewall/"


class Delete(DeleteView):
    template_name = "delete.html"
    model = Employee
    success_url = "/viewall/"