from rest_framework import serializers

from .models import Emprestimo


class EmprestimoSerializer(serializers.ModelSerializer):
    leitor_nome = serializers.CharField(source='leitor.nome', read_only=True)
    livro_titulo = serializers.CharField(source='livro.titulo', read_only=True)

    class Meta:
        model = Emprestimo
        fields = [
            'id', 'leitor', 'leitor_nome', 'livro', 'livro_titulo',
            'data_emprestimo', 'data_prevista', 'status',
        ]

    def validate(self, dados):
        data_emprestimo = dados.get('data_emprestimo')
        data_prevista = dados.get('data_prevista')

        if self.instance:
            if data_emprestimo is None:
                data_emprestimo = self.instance.data_emprestimo
            if data_prevista is None:
                data_prevista = self.instance.data_prevista

        if data_emprestimo and data_prevista and data_prevista <= data_emprestimo:
            raise serializers.ValidationError(
                'A data prevista precisa ser posterior à data do empréstimo.'
            )

        return dados
