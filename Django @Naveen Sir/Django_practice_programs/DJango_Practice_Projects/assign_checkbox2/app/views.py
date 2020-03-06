from django.shortcuts import render
def arjun(request):
    return render(request,"Index.html")
def karjun(request):
    d2={}
    movies=request.POST.get("M")
    cartoon=request.POST.get("C")
    images=request.POST.get("I")
    if movies= "mov" and cartoon="car"  images ="img":
        global w
        w="please select one"
    return render(request,"third.html", {"data": w})

def dispaly(request):
    d1={}
    temp= request.POST.get("M")
    temp2=request.POST.get("C")
    temp3=request.POST.get("I")
    if temp=="mov":
        global x
        x="1)Arjun Reddy", "2)Arya", "3)DJ", "4)Arya-2" "5)Pk"
        d1["mov"]=x
    if temp2=="car":
         global y
        y="1)Tom", "2)jerry","3)Been", "4)Doora" "5)Powerrangers"
        d1["car"]=y


    if temp3 == "img":
          global z
          z = "1).jpg", "2).png", "3).gif", "4).jpeg" "5).img"
          d1["img"] = z
    return render(request,"detsials.html",{"data":d1})

