# Generated by Django 4.2.2 on 2023-06-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_page_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template',
            field=models.CharField(choices=[('page.html', 'page.html'), ('home-page.html', 'home-page.html'), ('service-list.html', 'service-list.html'), ('contact.html', 'contact.html')], default=1, max_length=50, verbose_name='Использовать шаблон'),
        ),
    ]
