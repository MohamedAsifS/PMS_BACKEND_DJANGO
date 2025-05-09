# Generated by Django 5.1.7 on 2025-03-12 20:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, null=True)),
                ('company_location', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(choices=[('MCA', 'MCA'), ('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE')], max_length=8, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('marks', models.DecimalField(decimal_places=2, max_digits=30)),
                ('date_of_birth', models.DateField()),
                ('year', models.IntegerField(default=2025)),
                ('student_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management.department')),
            ],
        ),
        migrations.CreateModel(
            name='PlacementRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=30)),
                ('year', models.IntegerField(default=2025)),
                ('status', models.CharField(choices=[('selected', 'Selected'), ('rejected', 'Rejected'), ('shortlisted', 'Shortlisted'), ('waiting_list', 'Waiting List')], default='waiting_list', max_length=15)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.companytable')),
                ('department', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='management.department')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyDepartmentYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2025)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.companytable')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.department')),
            ],
            options={
                'unique_together': {('company', 'department', 'year')},
            },
        ),
    ]
