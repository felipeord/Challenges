from django.contrib import admin
from .models import Textualcontent, AnalysisReport
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
admin.site.register(Textualcontent)
admin.site.register(AnalysisReport)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name']
admin.site.register(CustomUser, CustomUserAdmin)


