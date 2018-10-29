# Generated by Django 2.1.1 on 2018-10-26 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0010_remove_projeto_vinculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='vinculo',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='disciplina.OrientadorAcademico'),
            preserve_default=False,
        ),
    ]