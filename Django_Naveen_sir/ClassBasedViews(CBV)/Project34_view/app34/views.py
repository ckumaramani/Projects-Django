from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse

def showindex(request):
    return render(request,"index.html")


class check(View):
    def post(self,request):
        return HttpResponse("post button Clicked")
    def get(self,request):
        return HttpResponse("get button Clicked")