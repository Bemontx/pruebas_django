from django.contrib import admin
from .models import *

# Register your models here.

# admin.site.register(Persona)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre','email')
    search_fields = ('nombre', 'email')