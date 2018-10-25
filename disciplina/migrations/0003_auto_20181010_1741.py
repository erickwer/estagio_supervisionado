# Generated by Django 2.1.1 on 2018-10-10 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0002_auto_20181009_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='identificador',
            field=models.IntegerField(choices=[(1, 'TCC'), (2, 'ESTÁGIO')], default=1, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='orientador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='disciplina.Professor'),
        ),
    ]