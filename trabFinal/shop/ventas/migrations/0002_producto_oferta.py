# Generated by Django 4.2.3 on 2023-08-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='oferta',
            field=models.BooleanField(default=False),
        ),
    ]