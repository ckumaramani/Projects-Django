from django.shortcuts import render
def content(request):
    d={
        101:{"name":"Arjun" , "age":23},
        102:{"name":"Hema", "age":22},
        103: {"name": "Mahe", "age": 23}
    }
    return render(request,"index.html",{"data":d})