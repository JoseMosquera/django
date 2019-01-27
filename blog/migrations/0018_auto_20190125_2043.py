# Generated by Django 2.1.5 on 2019-01-25 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20190125_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 19, 43, 35, 544793, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 25, 19, 43, 35, 543785, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
