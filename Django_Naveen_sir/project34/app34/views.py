from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


def Arjun(request):
    return render(request,"index.html")


class MyCBV(View):
    def post(self,request):
        return HttpResponse("PostButton Clicked")
    def get(self,request):
        return HttpResponse("Get Button Clicked")