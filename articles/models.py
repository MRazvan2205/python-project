from django.db import models


# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    created_by = models.IntegerField(null=True)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)


class Comments(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)
