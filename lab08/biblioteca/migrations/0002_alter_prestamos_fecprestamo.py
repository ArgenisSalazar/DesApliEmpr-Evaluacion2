# Generated by Django 4.1.2 on 2022-10-11 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamos',
            name='FecPrestamo',
            field=models.DateField(),
        ),
    ]