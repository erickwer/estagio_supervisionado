# Generated by Django 2.1.1 on 2018-10-17 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0004_auto_20181011_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrientadorAcademico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='disciplina.Aluno')),
                ('professor', models.ManyToManyField(null=True, to='disciplina.Professor')),
            ],
        ),
        migrations.RemoveField(
            model_name='banca',
            name='professores',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='banca',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='orientador',
        ),
        migrations.AddField(
            model_name='projeto',
            name='data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='notaFinal',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='periodo',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='projeto',
            name='professoresBanca',
            field=models.ManyToManyField(null=True, to='disciplina.Professor'),
        ),
        migrations.DeleteModel(
            name='Banca',
        ),
    ]
