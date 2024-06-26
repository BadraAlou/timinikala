# Generated by Django 5.0.6 on 2024-05-28 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_product_prix'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_filename',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]