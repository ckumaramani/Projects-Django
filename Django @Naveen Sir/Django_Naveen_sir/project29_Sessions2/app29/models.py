from django.db import models

class Staff(models.Model):
   username=models.CharField(primary_key=True, max_length=30)
   password=models.CharField(max_length=30)


class Feedback(models.Model):
    feedback=models.TextField()
