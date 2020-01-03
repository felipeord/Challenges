from django.contrib import admin
from .models import Textualcontent, AnalysisReport
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Textualcontent)
admin.site.register(AnalysisReport)
