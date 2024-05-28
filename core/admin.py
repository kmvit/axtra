from django.contrib import admin

from django.contrib.admin import ModelAdmin

from core.models import Page


class PageAdmin(ModelAdmin):
    list_display = ['title', 'category']
    list_filter = ['category',]

    def get_form(self, request, obj=None, **kwargs):
        # Proper kwargs are form, fields, exclude, formfield_callback
        if obj and obj.is_home_page:  # obj is not None, so this is a change page
            kwargs['fields'] = '__all__'
        else:  # obj is None, so this is an add page
            kwargs['fields'] = ['category', 'title', 'title_1', 'title_2', 'title_3', 'slug', 'meta_title',
                                'meta_description',
                                'preview_image', 'html_block_header', 'is_home_page',
                                'html_block_technology',
                                'content_one', 'content_two', 'template', 'faq_1_question', 'faq_1_answer',
                                'faq_2_question', 'faq_2_answer', 'faq_3_question', 'faq_3_answer',
                                'faq_4_question', 'faq_4_answer', 'faq_5_question', 'faq_5_answer', ]
        return super(PageAdmin, self).get_form(request, obj, **kwargs)


admin.site.register(Page, PageAdmin)
