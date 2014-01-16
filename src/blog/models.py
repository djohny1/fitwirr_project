from django.contrib.auth.models import User
from django.contrib import admin
from django.core.mail import send_mail
from taggit.managers import TaggableManager

from django.db import models
from django.db.models import permalink

class ActiveBlogManager(models.Manager):
    def get_query_set(self):
        return super(ActiveBlogManager, self).get_query_set().filter(is_active=True)
    
class Blog(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, null=True, blank=True)
    meta_keywords = models.CharField('Meta keywords', max_length=255, null=True, blank=True,
                                     help_text='Comma-delimited set SEO keywords for meta tag')
    meta_description = models.CharField('Meta Description', max_length=255, null=True, blank=True,
                                    help_text='Content for Description  meta tag')
    slug = models.SlugField()
    body = models.TextField()
    posted = models.DateTimeField(auto_now_add=True)
    pub_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    

    
    tags = TaggableManager()
    
    objects = models.Manager()
    active = ActiveBlogManager()
    
    def __unicode__(self):
        return '%s' % (self.title)
    
   
    
    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug })
    
class BlogImage(models.Model):
    blog = models.ForeignKey(Blog)
    image = models.ImageField(upload_to='blog/image/', null=True, blank=True)
    featured_image = models.BooleanField(default=False)
    
    def __unicode__(self):
        return str(self.image)
    

class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)
    
class Category(models.Model):
    blog = models.ManyToManyField(Blog)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    pub_date = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    
    objects = models.Manager()
    active = ActiveCategoryManager()
 
    
    def __unicode__(self):
        return '%s' % self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
    
    
    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug })
    
class BlogSearch(models.Model):
    q = models.CharField(max_length=50)
    blog = models.ForeignKey(Blog)
    search_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.IPAddressField()
    user = models.ForeignKey(User, null=True)
    
    def __unicode__(self,):
        return str(self.q)
    
    
