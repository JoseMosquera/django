# Generated by Django 2.1.5 on 2019-02-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles', verbose_name='Imagen de avatar'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Biografia'),
        ),
    ]
