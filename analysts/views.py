from rest_framework import generics

from .models import Analyst
from .serializers import AnalystSerializer

class AnalystView(generics.CreateAPIView):
    queryset = Analyst.objects.all()
    serializer_class = AnalystSerializer
