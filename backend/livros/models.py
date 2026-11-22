from django.db import models


class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo
