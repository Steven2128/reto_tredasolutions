# Generated by Django 3.2.9 on 2021-11-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='hora_consulta',
            field=models.DateTimeField(auto_now=True, verbose_name='Hora de consulta'),
        ),
    ]