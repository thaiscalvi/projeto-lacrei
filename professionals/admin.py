from django.contrib import admin
from .models import Professional

# Register your models here.
@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ("nome_social", "profissao", "contato")
    search_fields = ("nome_social", "profissao", "contato")