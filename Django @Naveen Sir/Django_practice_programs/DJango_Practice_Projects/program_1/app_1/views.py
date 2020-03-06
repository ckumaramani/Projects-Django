from django.shortcuts import render
def arjun(request):
    d1={
        "emply_id":101,
        "name":"ARJUN",
        "salary":125000,
        "status":True
    }
    return render(request,"index.html",d1)
