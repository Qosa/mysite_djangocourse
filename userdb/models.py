from django.db import models

# Create your models here.
class Users(models.Model):
    name = models.CharField(max_length=264,unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name