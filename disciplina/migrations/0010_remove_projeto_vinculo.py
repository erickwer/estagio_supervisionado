# Generated by Django 2.1.1 on 2018-10-26 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0009_auto_20181025_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='vinculo',
        ),
    ]