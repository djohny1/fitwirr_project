from django.conf import settings

from django.views.generic import ListView

from.models import News, NewsImage

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    

                       
    url(r'^$','press.views.press_room', name='press_room'),
    
    url(r'^logo/$','press.views.logo', name='logo'),
    
    url(r'^app_icon/$','press.views.app_icon', name='app_icon'),
    
    url(r'^list/$','press.views.list', name='list'),

    url(r'^press/view/(?P<slug>[^\.]+)', 'press.views.view_news', name='view_news_post'),
    
    
)

  
