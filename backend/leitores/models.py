from django.db import models


class Leitor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    matricula = models.CharField(max_length=20, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
