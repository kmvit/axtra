import datetime

from django.db import models
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.

WORK_CATEGORY = (
    ('visitka', 'Многостраничник'),
    ('shop', 'Интернет-магазин'),
    ('landing', 'Лэндинг'),
)


class Work(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Дружественный URL')
    meta_description = models.TextField(verbose_name='Мета описание')
    preview_image = models.FileField(upload_to='preview', verbose_name='Превью')
    image = models.FileField(upload_to='portfolio', blank=True, verbose_name='Изображение 1')
    image_2 = models.FileField(upload_to='portfolio', blank=True, verbose_name='Изображение 2')
    task = RichTextField(blank=True, verbose_name='Задача')
    solution = RichTextField(blank=True, verbose_name='Решение')
    technology = models.TextField(blank=True, verbose_name='Технологии')
    link_to_site = models.CharField(max_length=100, blank=True, verbose_name='Ссылка на сайт')
    category = models.CharField(max_length=50, choices=WORK_CATEGORY, default=1, blank=True,
                                verbose_name='Категория сайта')
    start_date = models.DateField(default=now, verbose_name='Дата начала')
    end_date = models.DateField(default=now, verbose_name='Дата окончания')
    client = models.CharField(max_length=255, blank=True, verbose_name='Клиент')
    show_on_home = models.BooleanField(default=0, verbose_name='Показывать на главной')

    class Meta:
        verbose_name = 'Работу'
        verbose_name_plural = 'Портфолио'
        ordering = ['-pk']

    def __str__(self):
        return self.title
