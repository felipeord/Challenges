from rest_framework import serializers
from .models import Textualcontent, CustomUser


class TextualcontentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Textualcontent
        fields = ('type', 'textorurl')
        #this must specify if you entered a url or a text


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', )