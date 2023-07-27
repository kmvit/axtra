import datetime

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now


class Case(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Дружественный URL')
    meta_title = models.TextField(blank=True,verbose_name='Мета заголовок')
    meta_description = models.TextField(verbose_name='Мета описание')
    preview_image = models.FileField(upload_to='preview', verbose_name='Превью')
    task = RichTextField(blank=True, verbose_name='Задача')
    solution = RichTextField(blank=True, verbose_name='Текст результата')
    ca = models.TextField(blank=True, verbose_name='Целевая аудитория')
    image = models.FileField(upload_to='case', blank=True, verbose_name='Изображение в поле решение')
    content_1 = RichTextField(blank=True, verbose_name='Текст стратегии')
    image_2 = models.FileField(upload_to='case', blank=True, verbose_name='Изображение идеи')
    content_2 = RichTextField(blank=True, verbose_name='Текст идеи')
    image_3 = models.FileField(upload_to='case', blank=True, verbose_name='Изображение еще идеи')
    content_3 = RichTextField(blank=True, verbose_name='Текст еще идеи')
    image_4 = models.FileField(upload_to='case', blank=True, verbose_name='Изображение результата')
    content_4 = RichTextField(blank=True, verbose_name='Текст технологии')
    link_to_site = models.CharField(max_length=100, blank=True, verbose_name='Ссылка на сайт')
    start_date = models.DateField(default=now, verbose_name='Дата начала')
    end_date = models.DateField(default=now, verbose_name='Дата окончания')
    client = models.CharField(max_length=255, blank=True, verbose_name='Клиент')
    show_on_home = models.BooleanField(default=0, verbose_name='Показывать на главной')

    class Meta:
        verbose_name = 'Кейс'
        verbose_name_plural = 'Кейсы'
        ordering = ['-pk']

    def __str__(self):
        return self.title
