# Generated by Django 5.0.3 on 2024-04-19 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva_turnos', '0005_alter_profesional_especialidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesional',
            name='especialidad',
            field=models.CharField(max_length=20),
        ),
    ]
