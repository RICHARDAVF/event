# Generated by Django 4.2 on 2023-04-30 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backgroundColor', models.CharField(max_length=150, verbose_name='Color de Fondo')),
                ('forengroudColor', models.CharField(max_length=150, verbose_name='Color por encima')),
            ],
        ),
    ]
