# Generated by Django 5.0.2 on 2024-02-11 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frutas', '0002_alter_fruta_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruta',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
