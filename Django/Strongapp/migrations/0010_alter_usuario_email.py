# Generated by Django 5.0.6 on 2024-07-05 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Strongapp', '0009_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False, unique=True),
        ),
    ]