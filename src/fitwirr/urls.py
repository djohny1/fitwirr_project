from django.conf import settings


from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root':settings.STATIC_ROOT
    }),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root':settings.MEDIA_ROOT
    }),
                       
    url(r'^press/', include('press.urls')),
    
    url(r'^blog/', include('blog.urls')),
   
    
    url(r'^profiles/$', 'profiles.views.all', name='all'),
    
    url(r'^members/(?P<username>\w+)/$', 'profiles.views.single_user', name='profile'),
    
    url(r'^members/(?P<username>\w+)/likes/$', 'profiles.views.single_user_likes', name='profile_likes'),
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$','exerciselibrary.views.list_all', name='all_exercise'),
    
    #url(r'^lib/', 'profiles.views.library', name='library'),
    url(r'^exerciselibrary//', include('exerciselibrary.urls')),
 
    
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^edit/$', 'profiles.views.edit_profile', name='edit_profile'),
  
    url(r'^contact/$', 'contact.views.contact_us', name='contact_us'),
    

    url(r'^search/', 'fitwirr.views.search', name='search'),
    
    url(r'^fitwirr/','exerciselibrary.views.fitwirr', name='fitwirr'),
    
    url(r'^about/','exerciselibrary.views.about', name='about'),
    url(r'^thankyou/', 'contact.views.thankyou', name='thankyou'),
    
    url(r'^team/', 'contact.views.team', name='team'),
    
    
    url(r'^terms/', 'contact.views.terms', name='terms'),
    
    url(r'^privacy/', 'contact.views.privacy', name='privacy'),
    
    
    
    
 )
handler404 = 'fitwirr.views.file_not_found_404'