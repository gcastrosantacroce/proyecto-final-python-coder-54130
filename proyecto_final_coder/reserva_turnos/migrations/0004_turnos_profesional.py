# Generated by Django 5.0.3 on 2024-04-05 15:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva_turnos', '0003_profesional'),
    ]

    operations = [
        migrations.AddField(
            model_name='turnos',
            name='profesional',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='reserva_turnos.profesional'),
        ),
    ]
