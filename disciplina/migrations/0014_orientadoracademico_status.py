# Generated by Django 2.1.1 on 2018-10-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplina', '0013_auto_20181025_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='orientadoracademico',
            name='status',
            field=models.CharField(max_length=200, null=True),
        ),
    ]