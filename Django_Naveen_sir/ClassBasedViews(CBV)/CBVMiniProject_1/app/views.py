from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView, RedirectView,UpdateView,DeleteView
from django.views.generic.base import View

from app.models import Employee,FeedBack,EnquiryForm






class Reegister(CreateView):
    template_name = "Register.html"
    success_url = '/register/'
    model = Employee
    fields = ('idno', 'name','designation','salary','contactno','username','password')



class Enquirypage(CreateView):
    model = EnquiryForm
    template_name = "Enquirypage.html"
    fields = ('name', 'gender', 'contactno', 'state', 'message')
    success_url = '/Enquirypage/'


def Register(request):
    return render(request,"Register.html")


def Save(request):
    idno=request.POST.get("t1")
    name=request.POST.get("t2")
    designation=request.POST.get("rd")
    salary=request.POST.get("t3")
    image = request.FILES["image"]
    contactno=request.POST.get("t4")
    username=request.POST.get("t5")
    password=request.POST.get("t6")
    Employee(idno=idno,name=name,designation=designation,image=image,salary=salary,contactno=contactno,username=username,password=password).save()
    return render(request,"Register.html",{"message":"Sucessfully Registered"})


def AdminLoginValidations(request):
    uname=request.POST.get("un")
    upass=request.POST.get("up")
    qs=Employee.objects.filter(username=uname,password=upass)
    if qs:
        return render(request,"welcomepage.html" ,{"name":uname})
    else:
        return render(request,"AdminLoginpage.html",{"msg":"!!!...Invalid Details...!!! Please Enter Valid Details"})


def Logout(request):
    return render(request,"AdminLoginpage.html",{"messagee":"Sucessfully Logout"})


def Viewall(request):
    qs=Employee.objects.all()
    return render(request,"viewall.html",{"data":qs})


def AdminLoginPage(request):
    return render(request, "AdminLoginpage.html")


def EmployeeLoginpage(request):
    return render(request,"EmployeeLoginPage.html")


def EmployeeWelcomePage(request):
    username=request.POST.get("un")
    password=request.POST.get("up")
    qs=Employee.objects.filter(username=username,password=password)
    if qs:
        return render(request,"EmployeeWelcomePage.html",{"data":username})
    else:
        return render(request,"EmployeeLoginPage.html",{"message":"!!!...Invalid Details...!!! Please Enter Valid Details"})


class update(UpdateView):
    template_name = "update.html"
    model = Employee
    fields = ('idno','name', 'designation', 'salary', 'contactno', 'username')
    success_url = "/viewall/"


class Delete(DeleteView):
    template_name = "Delete.html"
    model = Employee
    success_url = "/viewall/"