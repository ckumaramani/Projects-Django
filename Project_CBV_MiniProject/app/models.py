from django.db import models

class staff(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    Contactno=models.IntegerField()
    def __str__(self):
        return self.name
class register(models.Model):
    Idno = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Designation = models.CharField(max_length=30)
    Salary =models.DecimalField(max_digits=10, decimal_places=2)
    ContactNo =  models.IntegerField()
    State = models.CharField(max_length=30)
    Pincode =  models.IntegerField()

class feedbacks(models.Model):
    Name = models.CharField(max_length=30)
    ContactNo = models.IntegerField()
    EmailId = models.EmailField(max_length=30)
    state = models.CharField(max_length=30)
    Feedback = models.TextField()
