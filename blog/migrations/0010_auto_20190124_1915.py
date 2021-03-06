# Generated by Django 2.1.5 on 2019-01-24 18:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190124_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='foro',
            name='numero_posts',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 18, 15, 45, 777981, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publicacion',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 24, 18, 15, 45, 775986, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
