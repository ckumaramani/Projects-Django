from django.shortcuts import render

# Create your views here.
from app44.models import Article


def DisplayDetails(request):
    qs=Article.objects.all()
    return render(request,"index.html",{"data":qs})