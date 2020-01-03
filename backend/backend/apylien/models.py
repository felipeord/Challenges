from django.contrib.postgres.fields import JSONField
from django.db import models
from aylienapiclient import textapi

# from django_auto_one_to_one import AutoOneToOneModel
# Create your models here.
from pyexpat import model
# dependiendo de si quisieramos o no guardar los analysis hechos por un usuario se podría modificar el
# comportamiento de on_delete
# Should you treat every context - analysis as unique? or does it depend on the time passing and multiple
# versions of  the same analysis should be store in time?



class Textualcontent(models.Model):
    type = models.CharField(max_length=1000)
    textorurl = models.CharField(max_length=1000)
    extra = models.CharField(max_length=1000)
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.textorurl

    def save(self, *args, **kwargs):
        client = textapi.Client("ee583ac6", "bc2e37bf296a67827b18b98762d6b8eb")
        super(Textualcontent, self).save(*args, **kwargs)
        absa = client.Sentiment({'text': self.textorurl})
        an = AnalysisReport.objects.create(complete=1, result=absa, textualcontext=self)


class AnalysisReport(models.Model):
    complete = models.BooleanField(max_length=43, default=0)
    result = JSONField(default=dict)
    textualcontext = models.ForeignKey(Textualcontent, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.result
