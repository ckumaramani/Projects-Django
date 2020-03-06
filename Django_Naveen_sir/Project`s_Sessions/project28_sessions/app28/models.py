from django.db import models

class Sessions(models.Model):
    username=models.CharField(primary_key=True,max_length=30)
    password=models.CharField(max_length=30)


class Feedback(models.Model):
    username=models.CharField(max_length=30)
    feedback=models.TextField()