# Generated by Django 5.0.6 on 2024-07-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Strongapp', '0002_plan_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('contrasena', models.CharField(max_length=20)),
            ],
        ),
    ]
