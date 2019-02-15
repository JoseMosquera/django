# Generated by Django 2.1.5 on 2019-02-08 16:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0009_auto_20190206_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='participante',
            field=models.ManyToManyField(through='carreras.Posicion', to=settings.AUTH_USER_MODEL),
        ),
    ]
