# Generated by Django 4.2.2 on 2023-06-30 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_page_template'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='html',
            new_name='html_block_header',
        ),
    ]
