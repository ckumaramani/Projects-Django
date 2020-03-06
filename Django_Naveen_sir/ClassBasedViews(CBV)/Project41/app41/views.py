from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, UpdateView, DeleteView

from app41.models import Arjun


class Regitser(CreateView):
    template_name = "imdex.html"
    success_url = '/home/'
    model = Arjun
    fields = ('idno', 'name', 'designation', 'contactno')


class MyUpdateView(UpdateView):
    template_name = "update.html"
    model = Arjun
    fields = ('idno', 'name', 'designation', 'contactno')
    success_url = '/home/'


class MyDeleteView(DeleteView):
    template_name = "delete.html"
    model = Arjun
    success_url = '/home/'
