from django.urls import re_path as url
from . import views



app_name='post'
urlpatterns = [
    url(r'^$',views.all_posts,name='all_posts'),
    url(r'^(?P<id>\d+)$',views.posts,name='posts'),
    url(r'^create$',views.create_post,name='create_post'),
    url(r'^(?P<id>\d+)/edit$',views.edit_post,name='edit_post'),
]