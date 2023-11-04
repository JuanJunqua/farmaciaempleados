# Generated by Django 4.2.6 on 2023-11-04 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='encargado',
            name='empleo',
            field=models.CharField(default='encargado', max_length=64),
        ),
        migrations.AddField(
            model_name='mostrador',
            name='empleo',
            field=models.CharField(default='mostrador', max_length=64),
        ),
        migrations.AddField(
            model_name='subencargado',
            name='empleo',
            field=models.CharField(default='subencargado', max_length=64),
        ),
    ]