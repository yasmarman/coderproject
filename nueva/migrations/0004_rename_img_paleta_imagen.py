# Generated by Django 4.2.5 on 2023-10-20 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nueva', '0003_paleta_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paleta',
            old_name='img',
            new_name='imagen',
        ),
    ]
