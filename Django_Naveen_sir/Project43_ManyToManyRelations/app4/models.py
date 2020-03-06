from django.db import models

class Publications(models.Model):
    title=models.CharField(max_length=30)
    def __str__(self):
        return self.title

class Article(models.Model):
    headline=models.CharField(max_length=30)
    publication=models.ManyToManyField(Publications)


