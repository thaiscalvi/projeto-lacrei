from django.db import models
from django.utils import timezone

# Create your models here.
class Appointment(models.Model):
    professional = models.ForeignKey(
        "professionals.Professional",
        on_delete=models.PROTECT,   # evita apagar profissional com agendamentos
        related_name="appointments",
    )
    data = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Agendamento"
        verbose_name_plural = "Agendamentos"
        ordering = ("data",)

    def __str__(self):
        return f"{self.professional.nome_social} - {self.data:%d/%m/%Y %H:%M}"

    # (opcional) regra simples: não permitir agendar no passado
    def clean(self):
        super().clean()
        if self.data < timezone.now():
            from django.core.exceptions import ValidationError
            raise ValidationError({"data": "A data do agendamento não pode estar no passado."})