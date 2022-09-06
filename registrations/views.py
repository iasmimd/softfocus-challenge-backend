from django.shortcuts import get_object_or_404

from analysts.models import Analyst

from .models import Registration
from .serializers import RegistrationSerializer, DateLocationError

from rest_framework import generics
from rest_framework.views import  Response



class ResgitrationListView(generics.ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class RegistrationCreateView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def perform_create(self, serializer):
        analyst = get_object_or_404(Analyst, pk=self.kwargs["pk"])
        serializer.save(analyst=analyst)


class RegistrationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer



