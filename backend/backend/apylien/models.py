from django.contrib.postgres.fields import JSONField
from django.db import models
from aylienapiclient import textapi
from django.contrib.auth.models import AbstractUser
# from django_auto_one_to_one import AutoOneToOneModel
# Create your models here.
from pyexpat import model
# dependiendo de si quisieramos o no guardar los analysis hechos por un usuario se podría modificar el
# comportamiento de on_delete
# Should you treat every context - analysis as unique? or does it depend on the time passing and multiple
# versions of  the same analysis should be store in time?
from rest_framework import request


class CustomUser(AbstractUser):
    name = models.CharField(blank=True, max_length=255)


    def __str__(self):
        return self.username


class Textualcontent(models.Model):
    type = models.CharField(max_length=1000)
    textorurl = models.CharField(max_length=1000)
    extra = models.CharField(max_length=1000)
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    sentiment = models.BooleanField(max_length=2, default=0)
    classify = models.BooleanField(max_length=2, default=0)
    elsa = models.BooleanField(max_length=2, default=0)
    concept = models.BooleanField(max_length=2, default=0)
    summarize = models.BooleanField(max_length=2, default=0)


    def __str__(self):
        return self.textorurl

    def save(self, *args, **kwargs):
        client = textapi.Client("ee583ac6", "bc2e37bf296a67827b18b98762d6b8eb")

        super(Textualcontent, self).save(*args, **kwargs)
        if self.sentiment:
            sent = client.Sentiment({self.type: self.textorurl})
            sent = AnalysisReport.objects.create(complete=1, result=sent, textualcontext=self)
        if self.classify:
            cla = client.Classify({self.type: self.textorurl})
            cla = AnalysisReport.objects.create(complete=1, result=cla, textualcontext=self)
        if self.elsa:
            elsa = client.Elsa({self.type: self.textorurl})
            elsa = AnalysisReport.objects.create(complete=1, result=elsa, textualcontext=self)
        if self.concept:
            conc = client.Concepts({self.type: self.textorurl})
            conc = AnalysisReport.objects.create(complete=1, result=conc, textualcontext=self)
        if self.summarize:
            suma = client.Summarize({self.type: self.textorurl})
            suma = AnalysisReport.objects.create(complete=1, result=suma, textualcontext=self)

class AnalysisReport(models.Model):
    complete = models.BooleanField(max_length=43, default=0)
    result = JSONField(default=dict)
    textualcontext = models.ForeignKey(Textualcontent, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if (type(self.result == dict)):
            return ('nothing there')
        return self.result
