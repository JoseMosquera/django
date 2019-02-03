# Generated by Django 2.1.5 on 2019-01-30 07:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20190128_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 7, 49, 18, 614707, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 7, 49, 18, 610717, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]