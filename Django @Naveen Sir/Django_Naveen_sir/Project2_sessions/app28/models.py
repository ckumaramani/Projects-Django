from django.db import models
class Login(models.Model):
    username=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)


class FeedBack(models.Model):
    username=models.CharField(max_length=30)
    fb=models.TextField()
