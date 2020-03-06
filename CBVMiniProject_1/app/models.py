from django.db import models

class Employee(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10, decimal_places=2)
    contactno=models.IntegerField()
    image=models.ImageField(upload_to='Employees/')
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)


class EnquiryForm(models.Model):
    name=models.CharField(max_length=30)
    gender =models.CharField(max_length=30)
    contactno=models.IntegerField()
    state=models.CharField(max_length=30)
    message=models.TextField()

class FeedBack(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    contactno = models.IntegerField()
    feedback=models.TextField()