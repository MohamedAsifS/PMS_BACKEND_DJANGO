# Generated by Django 5.1.3 on 2025-03-29 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='department_name',
            field=models.CharField(max_length=8, null=True, unique=True),
        ),
    ]
