# Generated by Django 2.1.5 on 2019-02-04 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0006_auto_20190204_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entreno',
            name='imagen',
            field=models.ImageField(upload_to='entrenos', verbose_name='Imagen'),
        ),
    ]
