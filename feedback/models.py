from django.db import models

# Create your models here.
class feedback(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    feedback = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.name