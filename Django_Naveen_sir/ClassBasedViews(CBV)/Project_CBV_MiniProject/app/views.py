from django.shortcuts import render
from django.views.generic import FormView
from app.forms import Arjun, Feedback, Register
from app.models import register,feedbacks


class Loginpage(FormView):
    form_class = Arjun
    template_name = "loginpage.html"


class Aboutus(FormView):
    form_class = Feedback
    template_name = "about us.html"
    success_url = "/aboutus/"

    def form_valid(self, form):
       if form.is_valid():
            name = form.cleaned_data.get("Name")
            contactno = form.cleaned_data.get("ContactNo")
            state = form.cleaned_data.get("State")
            email=form.cleaned_data.get("EmailId")
            feedback=form.cleaned_data.get("Feedback")
            feedbacks(Name=name,ContactNo=contactno,EmailId=email,state=state,Feedback=feedback).save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class Register(FormView):
    template_name = "register.html"
    form_class = Register
    success_url='/home/'

    def form_valid(self, form):
     if form.is_valid():
        idno=form.cleaned_data.get("Idno")
        name=form.cleaned_data.get("Name")
        designation=form.cleaned_data.get("Designation")
        salary=form.cleaned_data.get("Salary")
        contactno=form.cleaned_data.get("ContactNo")
        state=form.cleaned_data.get("State")
        pincode=form.cleaned_data.get("Pincode")
        register(Idno=idno,Name=name,Salary=salary,Designation=designation,ContactNo=contactno,State=state,Pincode=pincode).save()
        return super().form_valid(form)
     else:
        return self.form_invalid(form)