# Generated by Django 5.0.6 on 2024-05-30 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_warehouse_latitude_warehouse_longitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehouse',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='longitude',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='name',
        ),
    ]