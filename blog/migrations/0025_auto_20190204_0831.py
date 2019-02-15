# Generated by Django 2.1.5 on 2019-02-04 07:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20190130_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 7, 31, 45, 891678, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 7, 31, 45, 888100, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
