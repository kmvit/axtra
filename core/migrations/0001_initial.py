# Generated by Django 4.2.2 on 2023-06-27 19:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Дружественный URL')),
                ('meta_title', models.TextField(blank=True, null=True, verbose_name='Meta Title')),
                ('meta_description', models.TextField(blank=True, null=True, verbose_name='Meta Description')),
                ('preview_image', models.FileField(blank=True, null=True, upload_to='preview')),
                ('is_home_page', models.BooleanField(default=False, verbose_name='Назначить главной страницей')),
                ('html', models.TextField(blank=True, null=True, verbose_name='Html код')),
                ('content_one', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Для кого подойдет')),
                ('content_two', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Что получаете при заказе')),
                ('portfolio', models.CharField(choices=[('visitka', 'Многостраничник'), ('shop', 'Интернет-магазин'), ('landing', 'Лэндинг')], default=1, max_length=50, verbose_name='Какую категорию работ выводить')),
            ],
            options={
                'verbose_name': 'Страницу',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
