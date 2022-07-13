from django.db import models

# Create your models here.

class keyword(models.Model):
    data = models.CharField(max_length=250,null=True,blank=True)
    def __str__(self) -> str:
        return self.data