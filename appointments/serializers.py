from rest_framework import serializers
from django.utils import timezone
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    professional_nome = serializers.CharField(source="professional.nome_social", read_only=True)

    class Meta:
        model = Appointment
        fields = ["id", "professional", "professional_nome", "data", "created_at", "updated_at"]

    def validate_data(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("A data do agendamento não pode estar no passado.")
        return value
