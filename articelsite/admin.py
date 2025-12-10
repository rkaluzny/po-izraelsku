from django.contrib import admin
from .models import Articel
from django_summernote.widgets import SummernoteWidget 
from django.db import models 

# Register your models here.

class ArticelAdmin(admin.ModelAdmin): 

     formfield_overrides = { 
            models.TextField: {'widget': SummernoteWidget}, 
     } 

admin.site.register(Articel, ArticelAdmin)