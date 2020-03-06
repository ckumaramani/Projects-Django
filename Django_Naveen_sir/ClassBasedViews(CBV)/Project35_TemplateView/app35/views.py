from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.base import View


class show(TemplateView):
    template_name = "index.html"

class courses(TemplateView):
    template_name = "courses.html"

