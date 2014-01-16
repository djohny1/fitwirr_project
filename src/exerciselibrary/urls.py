from django.conf import settings

from django.conf.urls import patterns, include, url

from django.views.generic import ListView, DetailView
# Uncomment the next two lines to enable the admin:
from .models import Exercise, Category


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('exerciselibrary.views',
    #url(r'^$','list_all', name='all_exercises'),
    url(r'^$','list_all', name='all'),
    
    url(r'^(?P<slug>.*)/edit/','edit_exercise', name='edit_exercise'),
    
    url(r'^add/','add_exercise', name='add_exercise'),
    
    url(r'^images/like_or_dislike/(?P<image_id>\d+)/$','like_or_dislike_exercise_image', name='like_or_dislike_exercise_image'),
    
        
    url(r'^search/$','search', name="exerciselibrary_search"),
    
    url(r'^(?P<slug>.*)/images/','manage_exercise_image', name='manage_exercise_image'),
    
    url(r'^(?P<slug>.*)/$','single', name='single_exercise'),
    
   
    
    url(r'^tag/(?P<tag>[a-zA-Z\s]*)','exercise_tagpage', name='exercise_tagpage'),
   
    
    #url(r'^tag/(?P<tag>\w+)$','exercise_tagpage'),
  
    
  
 
    
)
