# Generated by Django 2.1.5 on 2019-02-07 18:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20190207_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 18, 6, 2, 273953, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 7, 18, 6, 2, 271959, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]