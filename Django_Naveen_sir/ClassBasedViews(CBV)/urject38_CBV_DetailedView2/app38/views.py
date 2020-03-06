from django.shortcuts import render
from django.views.generic import DetailView

from app38.models import Arjun


class allempids(DetailView):
    template_name = "view.html"
    model = Arjun
