from django.db import models

# Create your models here.
class Professional(models.Model):
    nome_social = models.CharField(max_length=150)
    profissao = models.CharField(max_length=100)
    endereco = models.TextField(blank=True)
    contato = models.CharField(max_length=120)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"
        ordering = ("nome_social",)

    def __str__(self):
        return f"{self.nome_social} ({self.profissao})"