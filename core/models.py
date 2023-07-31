from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse

TEMPLATES = (
    ('page.html', 'page.html'),
    ('home-page.html', 'home-page.html'),
    ('service-list.html', 'service-list.html'),
    ('contact.html', 'contact.html'),
)


class Page(models.Model):
    CATEGORY = (
        ('web','Создание сайтов'),
        ('mobile', 'Мобильная разработка'),
        ('marketing', ' Реклама')
    )
    category = models.CharField(max_length=100, choices=CATEGORY, default='web', verbose_name='Категория страницы')
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Дружественный URL')
    meta_title = models.TextField(blank=True, null=True, verbose_name='Meta Title')
    meta_description = models.TextField(blank=True, null=True, verbose_name='Meta Description')
    preview_image = models.FileField(upload_to='page', blank=True, null=True)
    title_1 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок первый')
    title_2 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок второй')
    title_3 = models.CharField(max_length=200, blank=True, verbose_name='Заголовок третий')
    html_block_header = models.TextField(blank=True, null=True, verbose_name='Html код')
    html_block_technology = models.TextField(blank=True, null=True, verbose_name='Html технологии')
    content_one = RichTextField(blank=True, null=True, verbose_name='Для кого подойдет')
    content_two = RichTextField(blank=True, null=True, verbose_name='Что получаете при заказе')

    phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    mobile_phone = models.CharField(max_length=20, blank=True, verbose_name='Мобильный')
    email = models.EmailField(blank=True, verbose_name='Почта')
    address = models.TextField(blank=True, verbose_name='Адрес')
    instagram = models.CharField(max_length=100, blank=True, null=True, verbose_name='Инстаграмм')
    vk = models.CharField(max_length=100, blank=True, null=True, verbose_name='Вконтакте')
    is_home_page = models.BooleanField(default=False, verbose_name='Назначить главной страницей')
    template = models.CharField(max_length=50, choices=TEMPLATES, default=1, verbose_name='Использовать шаблон')

    faq_1_question = models.CharField(max_length=255, blank=True, verbose_name='Вопрос 1')
    faq_1_answer = models.TextField(blank=True, verbose_name='Ответ 1')
    faq_2_question = models.CharField(max_length=255, blank=True, verbose_name='Вопрос 2')
    faq_2_answer = models.TextField(blank=True, verbose_name='Ответ 2')
    faq_3_question = models.CharField(max_length=255, blank=True, verbose_name='Вопрос 3')
    faq_3_answer = models.TextField(blank=True, verbose_name='Ответ 3')
    faq_4_question = models.CharField(max_length=255, blank=True, verbose_name='Вопрос 4')
    faq_4_answer = models.TextField(blank=True, verbose_name='Ответ 4')
    faq_5_question = models.CharField(max_length=255, blank=True, verbose_name='Вопрос 5')
    faq_5_answer = models.TextField(blank=True, verbose_name='Ответ 5')

    class Meta:
        verbose_name = 'Страницу'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pages:page', kwargs={'slug': self.slug})


