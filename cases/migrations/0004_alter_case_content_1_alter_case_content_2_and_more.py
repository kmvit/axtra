# Generated by Django 4.2.2 on 2023-07-31 10:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0003_case_meta_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='content_1',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст стратегии'),
        ),
        migrations.AlterField(
            model_name='case',
            name='content_2',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст идеи'),
        ),
        migrations.AlterField(
            model_name='case',
            name='content_3',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст еще идеи'),
        ),
        migrations.AlterField(
            model_name='case',
            name='content_4',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст технологии'),
        ),
        migrations.AlterField(
            model_name='case',
            name='image',
            field=models.FileField(blank=True, upload_to='case', verbose_name='Изображение в поле решение'),
        ),
        migrations.AlterField(
            model_name='case',
            name='image_2',
            field=models.FileField(blank=True, upload_to='case', verbose_name='Изображение идеи'),
        ),
        migrations.AlterField(
            model_name='case',
            name='image_3',
            field=models.FileField(blank=True, upload_to='case', verbose_name='Изображение еще идеи'),
        ),
        migrations.AlterField(
            model_name='case',
            name='image_4',
            field=models.FileField(blank=True, upload_to='case', verbose_name='Изображение результата'),
        ),
        migrations.AlterField(
            model_name='case',
            name='solution',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Текст результата'),
        ),
    ]
