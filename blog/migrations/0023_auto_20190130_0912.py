# Generated by Django 2.1.5 on 2019-01-30 08:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20190130_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 8, 12, 14, 50839, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 30, 8, 12, 14, 48519, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
