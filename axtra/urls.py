"""
URL configuration for axtra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import TemplateView

from axtra import settings
from core.views import ContactView, PageSiteMap, BlogSiteMap

sitemaps = {
    'Pagesitemap': PageSiteMap,
    'Blogsitemap': BlogSiteMap,
}

handler404 = 'core.views.view_404'

urlpatterns = [
      path('admin/', admin.site.urls),
      path('contact/', ContactView.as_view(), name='contact'),
      path('portfolio/', include('portfolio.urls', namespace='portfolio')),
      path('cases/', include('cases.urls', namespace='case')),
      path('blog/', include('blog.urls', namespace='blog')),
      path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
           name='django.contrib.sitemaps.views.sitemap'),
      path(
          "robots.txt",
          TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
      path('ckeditor/', include('ckeditor_uploader.urls')),
      path('', include('core.urls', namespace='core')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
