from django.shortcuts import render
def show(request):
        d1 =  {

         "101": {"name": "Arjun", "salary": 100000.00},
         "102": {"name": "Arun", "salary": 120000.00},
         "103": {"name": "Akash", "salary": 102000.00}}
        return render(request,"index.html",{"data":d1})