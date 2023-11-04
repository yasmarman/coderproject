# Generated by Django 4.2.5 on 2023-11-03 23:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comentarios', '0003_rename_autor_comentario_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]