# Generated by Django 5.0.2 on 2024-02-11 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]