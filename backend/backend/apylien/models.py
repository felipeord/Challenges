from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Textualcontent(models.Model):
    type = models.CharField(max_length=1000)
    textorurl = models.CharField(max_length=1000)

    def __str__(self):
        return self.textorurl


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
