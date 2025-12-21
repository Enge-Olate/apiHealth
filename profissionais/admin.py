from django.contrib import admin
from .models import Profissional

# Register your models here.
@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especialidade', 'crm')
    search_fields= ('nome', 'crm')
    list_filter= ('id', )
    readonly_fields= ('id', )