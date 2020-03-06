from django.shortcuts import render
from django.shortcuts import render
def arjun(request):
    return render(request,"index.html")
def karjun(request):
    at=request.POST.getlist("cb")
     data={"movies":['Arjun Reddy','Arya','Arya-2','Dj','pk'],
          "catoons":['c1','c2,'c3,'c4','c5'],
          "images": ['i1', 'i2,'i3, 'i4', 'i5']}
     request render(request,"details.html",{"at":at,"data":data})


