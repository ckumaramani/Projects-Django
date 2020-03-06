from django.shortcuts import render
from reportlab.pdfgen import canvas
from .models import employee
from django.http import HttpResponse
def arjun(request):
    return render(request,"index.html")


def karjun(request):

    req=HttpResponse(content_type='application\pdf')
    req['content_Disposition'] = 'attachment; filename="employees.pdf"'
    pdf = canvas.Canvas(req)
    pdf.setFont("Times-Roman", 50)
    qs = employee.objects.all()
    y = 800
    for x in qs:
        data = str(x.idno) + " " + x.name + " " + str(x.salary)
        pdf.drawString(0, y, data)
        y -= 150
    pdf.showPage()
    pdf.save()
    return req