# Generated by Django 2.1.5 on 2019-01-26 19:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='descripcion',
            field=ckeditor.fields.RichTextField(verbose_name='Descripcion'),
        ),
    ]
