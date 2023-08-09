from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import Blog, Category


class BlogList(generic.ListView):
    template_name = 'blog/blog_list.html'
    queryset = Blog.objects.all().order_by('-date_born')

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['my_title'] = 'Полезные статьи'
        context['my_description'] = 'Полезные статьи'
        return context


class BlogDetail(generic.DetailView):
    template_name = 'blog/blog_detail.html'
    queryset = Blog.objects.all().order_by('-date_born')

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        context['blog_list'] = Blog.objects.all().exclude(id=self.object.id)[:3]
        return context


class CategoryList(generic.ListView):
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        return Blog.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        try:
            context['my_title'] = Blog.objects.filter(category__slug=self.kwargs['slug']).first().category
        except Category.DoesNotExist:
            raise Http404
        context['my_description'] = 'Полезные статьи о ' + Blog.objects.filter(
            category__slug=self.kwargs['slug']).first().category.title

        return context
