from rest_framework import viewsets

from .models import Leitor
from .serializers import LeitorSerializer


class LeitorViewSet(viewsets.ModelViewSet):
    queryset = Leitor.objects.all()
    serializer_class = LeitorSerializer
