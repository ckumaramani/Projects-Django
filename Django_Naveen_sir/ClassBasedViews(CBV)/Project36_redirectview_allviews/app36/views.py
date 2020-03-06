from django.shortcuts import render
from django.views.generic import RedirectView
from django.views.generic.base import View, TemplateView


class show(TemplateView):
    template_name="fb.html"



