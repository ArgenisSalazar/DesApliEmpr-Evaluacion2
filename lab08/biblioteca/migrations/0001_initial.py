# Generated by Django 4.1.2 on 2022-10-11 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('idAutor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('idPrestamo', models.AutoField(primary_key=True, serialize=False)),
                ('idLibro', models.IntegerField(default=0)),
                ('idUsuario', models.IntegerField(default=0)),
                ('FecPrestamo', models.DateTimeField()),
                ('FecDevolucion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('numUsuario', models.IntegerField(default=0)),
                ('nif', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=20)),
                ('prestamo', models.ManyToManyField(to='biblioteca.prestamos')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('idLibro', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.IntegerField(default=0)),
                ('titulo', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=100)),
                ('editorial', models.CharField(max_length=100)),
                ('numpags', models.SmallIntegerField(default=0)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.autor')),
                ('prestamo', models.ManyToManyField(to='biblioteca.prestamos')),
            ],
        ),
    ]
