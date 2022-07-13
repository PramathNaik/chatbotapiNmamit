from re import T
from django.db import models
from django.forms import CharField
from keywords.models import keyword
# Create your models here.
class QNA(models.Model):
    question = models.CharField(max_length=250,null=True,blank=True)
    answer = models.TextField(blank=True)
    keywords = models.ManyToManyField(keyword,blank=True)
    def __str__(self) -> str:
        return self.question

