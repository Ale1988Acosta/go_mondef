# Generated by Django 4.0.4 on 2022-06-08 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Go_mon', '0005_alter_cuidador_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloque',
            name='hora',
            field=models.CharField(max_length=20, verbose_name='Intervalo de hora'),
        ),
    ]
