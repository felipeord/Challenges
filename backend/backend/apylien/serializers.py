from rest_framework import serializers
from .models import Textualcontent, AnalysisReport, CustomUser


class TextualcontentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Textualcontent
        fields = ('id', 'type', 'textorurl', 'customuser', 'sentiment', 'classify', 'elsa', 'concept', 'summarize' )
        #this must specify if you entered a url or a text

class AnalysisReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnalysisReport
        fields = ('complete', 'result', 'textualcontext' )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'username', )

class AnalysisPorUsuarioSerializer(serializers.ModelSerializer):
        class Meta:
            model = AnalysisReport
            fields = ('result', 'textualcontext')