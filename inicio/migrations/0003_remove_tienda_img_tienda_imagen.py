# Generated by Django 4.2.5 on 2023-10-20 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_tienda_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tienda',
            name='img',
        ),
        migrations.AddField(
            model_name='tienda',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='avatares'),
        ),
    ]
