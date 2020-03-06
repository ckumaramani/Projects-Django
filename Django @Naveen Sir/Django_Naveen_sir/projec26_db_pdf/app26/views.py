from django.shortcuts import render
from django.http import HttpResponse
from .models import employee
from reportlab.pdfgen import canvas

def arjun(request):
    return render(request,"index.html")


def downloadpdf(request):
    res=HttpResponse(content_type="application/pdf")
    res['content_Disposition']='attachment; filename="employees.pdf"'
    pdf=canvas.Canvas(res)
    pdf.setFont("Times-Roman",50)
    qs=employee.objects.all()
    y=800
    for x in qs:
        data=str(x.idno)+" "+x.name+" "+str(x.salary)
        pdf.drawString(0,y,data)
        y-=150
    pdf.showPages()
    pdf.save()
    return res
