from django.contrib import admin
from .models import Appointment
# Register your models here.

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("professional", "data")
    list_filter = ("professional",)
    search_fields = ("professional__nome_social",)