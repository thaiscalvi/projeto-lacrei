from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.select_related("professional").order_by("data")
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        professional_id = self.request.query_params.get("professional_id")
        if professional_id:
            qs = qs.filter(professional_id=professional_id)
        return qs
