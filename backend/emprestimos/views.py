from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Emprestimo
from .serializers import EmprestimoSerializer


class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    @action(detail=False, methods=['get'])
    def abertos(self, request):
        emprestimos = Emprestimo.objects.filter(status='ABERTO')
        serializer = self.get_serializer(emprestimos, many=True)
        return Response(serializer.data)
