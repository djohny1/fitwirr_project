from django.conf import settings

from django.conf.urls import patterns, include, url


from django.views.generic import ListView, DetailView

from django.views.generic import ListView
#from django.conf.urls.defaults import *
from .models import Blog, Category


urlpatterns = patterns('',
    url(r'^$','blog.views.index', name='index'),
    #(r'^$', 'blog.views.index'),
    url(r'^blog/view/(?P<slug>[^\.]+)', 'blog.views.view_post', name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+)', 'blog.views.view_category', name='view_blog_category'),
    
  
   
    #url(r'^tag/(?P<tag>\w+)$','blog.views.tagpage', name='tagpage'),
    
    url(r'^tag/(?P<tag>.*)$','blog.views.tagpage', name='tagpage'),
    

  
    #url(r'^results$','blog.views.results', name='search_results'),
    url(r'^search/$','blog.views.search', name="blog_search"),
    
    (r"^archives/$"  , ListView.as_view(queryset=Blog.objects.all().order_by('-pub_date'), template_name='archives.html')),
    
)