# Generated by Django 2.1.5 on 2019-02-06 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0008_auto_20190205_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posicion',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carrera', to='carreras.Carrera'),
        ),
        migrations.AlterField(
            model_name='posicion',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]