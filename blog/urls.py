from django.urls import path
from .views import BlogList, BlogDetail,CategoryList

app_name="blog"

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('<slug>', CategoryList.as_view(), name='category_list'),
    path('<category_slug>/<slug>/', BlogDetail.as_view(), name='blog_detail'),

]