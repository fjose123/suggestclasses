# Generated by Django 3.0.6 on 2020-05-08 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0066_auto_20200427_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='turma',
            name='horarios',
            field=models.ManyToManyField(related_name='turmas', to='core.Horario'),
        ),
    ]
