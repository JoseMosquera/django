# Generated by Django 2.1.5 on 2019-02-04 07:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0002_entreno_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='participante',
            field=models.ManyToManyField(blank=True, null=True, through='carreras.Posicion', to=settings.AUTH_USER_MODEL),
        ),
    ]