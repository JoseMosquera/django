# Generated by Django 2.1.5 on 2019-01-24 17:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190124_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 17, 37, 11, 395903, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 17, 37, 11, 393909, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
