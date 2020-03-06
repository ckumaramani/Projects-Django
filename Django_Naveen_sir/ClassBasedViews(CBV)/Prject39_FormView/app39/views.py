from django.shortcuts import render

from django.views.generic import FormView

from app39.models import Arjun
from .forms import arjun
class MYRegisterform(FormView):
    form_class = arjun
    template_name = "index.html"
    success_url = '/home/'
    def form_valid(self, form):
        if form.is_valid():
            id=form.cleaned_data.get("id")
            name=form.cleaned_data.get("na")
            salary=form.cleaned_data.get("sal")
            uname=form.cleaned_data.get("un")
            password=form.cleaned_data.get("pas")
            Arjun(idno=id,name=name,password=password,salary=salary,username=uname).save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)