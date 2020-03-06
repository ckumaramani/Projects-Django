from django.shortcuts import render

# Create your views here.
from app4.models import Article


def DisplayDetails(request):
    qs=Article.objects.all()
    return render(request,"viewall.html",{"data":qs})