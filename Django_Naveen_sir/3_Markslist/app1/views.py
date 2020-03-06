from django.shortcuts import render
def function(request):
        d1 = {101: {"name": "A", "class": "10", "marks": [65, 95, 85, 50, 45, 99]},
         102: {"name": "B", "class": "10", "marks": [45, 85, 52, 58, 49, 90]},
         103: {"name": "C", "class": "10", "marks": [68, 85, 58, 65, 85, 88]},
         104: {"name": "D", "class": "10", "marks": [65, 90, 85, 55, 48, 97]},
         105: {"name": "E", "class": "10", "marks": [64, 96, 87, 54, 41, 93]}}
        return render(request,"arjun.html","data.d1")