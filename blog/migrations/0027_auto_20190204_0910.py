# Generated by Django 2.1.5 on 2019-02-04 08:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20190204_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 8, 10, 39, 890446, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 8, 10, 39, 886448, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
