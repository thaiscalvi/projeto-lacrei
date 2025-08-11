from rest_framework import viewsets
from .models import Professional
from .serializers import ProfessionalSerializer

class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all().order_by("nome_social")
    serializer_class = ProfessionalSerializer
