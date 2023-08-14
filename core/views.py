from django.contrib.sitemaps import Sitemap
from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView

from blog.models import Blog
from cases.models import Case
from core.models import Page
from portfolio.models import Work


class PageSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Page.objects.all()


class BlogSiteMap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Blog.objects.all()


class PageView(DetailView):
    model = Page

    def get_template_names(self):
        return 'core/' + self.object.template

    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        return context


class HomePage(DetailView):
    model = Page
    template_name = 'core/home_page.html'

    def get_object(self, queryset=None):
        return Page.objects.get(is_home_page=True)

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['portfolio_list'] = Work.objects.filter(show_on_home=True)
        context['blog_list'] = Blog.objects.all()[:3]
        context['case_list'] = Case.objects.all()
        return context


class ContactView(DetailView):
    template_name = 'core/contact.html'

    def get_object(self, queryset=None):
        return Page.objects.get(slug='contact')


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')  # or redirect('name-of-index-url')
