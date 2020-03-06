from django.shortcuts import render


#def show(request):
   # return render(request,"index.html")
from django.views.generic import TemplateView


class showindex(TemplateView):
    template_name = "index.html"