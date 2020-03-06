from django.db import models

class Staff(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    contactno=models.IntegerField()
    designation=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    Address=models.TextField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    image=models.ImageField(upload_to='media/arjun')



class Enquiry(models.Model):
    name=models.CharField(max_length=30, primary_key=True)
    gender=models.CharField(max_length=30)
    contactno=models.IntegerField()
    area=models.TextField()
    state=models.CharField(max_length=30)



