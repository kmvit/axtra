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
        context['blog_list'] = Blog.objects.all().exclude(id=self.object.id)[
                               :3]
        return context


class CategoryList(generic.DetailView):
    template_name = 'blog/category.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryList, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        try:
            context['category'] = Category.objects.get(
                slug=self.kwargs['slug'])
            context['blog_list'] = Blog.objects.filter(
                category__slug=self.kwargs['slug'])
        except Category.DoesNotExist:
            Http404
        return context
