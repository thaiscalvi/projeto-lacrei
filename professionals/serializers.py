from rest_framework import serializers
from .models import Professional

class ProfessionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional
        fields = ["id", "nome_social", "profissao", "endereco", "contato", "created_at", "updated_at"]
