from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from professionals.views import ProfessionalViewSet
from appointments.views import AppointmentViewSet

router = DefaultRouter()
router.register(r'professionals', ProfessionalViewSet, basename='professional')
router.register(r'appointments', AppointmentViewSet, basename='appointment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
