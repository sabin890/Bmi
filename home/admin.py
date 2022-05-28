from django.contrib import admin
from .models import Bmi
# Register your models here.
@admin.register(Bmi)
class BmiModelAdmin(admin.ModelAdmin):
    list_display =['id','hight','weight','age','result','suggest','user']