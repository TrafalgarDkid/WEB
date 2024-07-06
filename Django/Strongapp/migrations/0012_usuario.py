# Generated by Django 5.0.6 on 2024-07-05 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Strongapp', '0011_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
    ]
