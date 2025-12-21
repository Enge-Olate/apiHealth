from django.contrib import admin
from .models import Consulta, Profissional, Paciente

# Register your models here.
@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display=('paciente', 'profissional', 'data', 'status')
