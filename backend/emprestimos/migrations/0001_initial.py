import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('leitores', '0001_initial'),
        ('livros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_emprestimo', models.DateField()),
                ('data_prevista', models.DateField()),
                ('status', models.CharField(choices=[('ABERTO', 'Aberto'), ('DEVOLVIDO', 'Devolvido')], default='ABERTO', max_length=10)),
                ('leitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leitores.leitor')),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livros.livro')),
            ],
        ),
    ]
