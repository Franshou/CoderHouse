# Generated by Django 3.2.9 on 2021-12-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=40)),
                ('catedra', models.CharField(max_length=40)),
            ],
        ),
    ]
