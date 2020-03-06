from django.shortcuts import render
from django.core.paginator import Paginator
# Create your views here.
from app46.models import Employee


def Pagenation(request):
    pagno=request.GET.get("pno")
    list=Employee.objects.all()
    p=Paginator(list,2)
    if pagno:
        res=p.page(pagno)
    else:
        pagno=1
        res=p.page(pagno)
    return render(request,"main.html",{"result":res})

