# Generated by Django 4.2.5 on 2023-11-03 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0006_alter_comentario_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='autor',
        ),
    ]
