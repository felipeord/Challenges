from rest_framework import serializers
from .models import Textualcontent, AnalysisReport


class TextualcontentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Textualcontent
        fields = ('id', 'type', 'textorurl', 'extra' )
        #this must specify if you entered a url or a text

class AnalysisReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnalysisReport
        fields = ('complete', 'result' )