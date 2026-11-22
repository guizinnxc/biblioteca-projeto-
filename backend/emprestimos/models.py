from django.db import models

from leitores.models import Leitor
from livros.models import Livro


class Emprestimo(models.Model):
    STATUS_CHOICES = [
        ('ABERTO', 'Aberto'),
        ('DEVOLVIDO', 'Devolvido'),
    ]

    leitor = models.ForeignKey(Leitor, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField()
    data_prevista = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ABERTO',
    )

    def __str__(self):
        return f'{self.livro} - {self.leitor}'
