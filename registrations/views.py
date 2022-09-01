from django.shortcuts import get_object_or_404

from analysts.models import Analyst
from analysts.serializers import AnalystSerializer

from .models import Registration
from .serializers import RegistrationSerializer

from rest_framework import generics


class RegistrationView(generics.ListCreateAPIView):
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        analyst = get_object_or_404(Analyst, pk=self.kwargs["pk"])

        serializer.save(analyst=analyst)

    def get_queryset(self):
        analyst = get_object_or_404(Analyst, pk=self.kwargs["pk"])

        return Registration.objects.filter(analyst=analyst).order_by("id")
