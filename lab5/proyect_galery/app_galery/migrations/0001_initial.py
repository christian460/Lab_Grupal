# Generated by Django 4.2.2 on 2023-06-18 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
                ('precio_pen', models.DecimalField(decimal_places=2, max_digits=7)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes')),
            ],
        ),
    ]
