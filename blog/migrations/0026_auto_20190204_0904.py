# Generated by Django 2.1.5 on 2019-02-04 08:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20190204_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 8, 4, 57, 938050, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 8, 4, 57, 934057, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
