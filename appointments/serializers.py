from rest_framework import serializers
from django.utils import timezone
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    professional_nome = serializers.CharField(source="professional.nome_social", read_only=True)

    class Meta:
        model = Appointment
        fields = ["id", "professional", "professional_nome", "data", "created_at", "updated_at"]

    def validate_data(self, value):
        if value is None:
            raise serializers.ValidationError("A data do agendamento é obrigatória.")
        # exige data futura (tolerância de 1 minuto)
        if value < timezone.now() + timezone.timedelta(minutes=1):
            raise serializers.ValidationError("A data do agendamento deve ser no futuro.")
        return value
