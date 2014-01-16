from django.db import models
from django.db.models import permalink

# Create your models here.

class News(models.Model):
    headline = models.CharField(max_length=100)
    sub_headline = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField()
    pub_date = models.DateTimeField(null=True, blank=True)
    website = models.URLField()
    active = models.BooleanField(default=True)
    
    def __unicode__(self):
        return str(self.headline)

    @permalink
    def get_absolute_url(self):
        return ('view_news_post', None, {'slug': self.slug })
    

    
class NewsImage(models.Model):
    news = models.ForeignKey(News)
    image = models.ImageField(upload_to='news/image/', null=True, blank=True)
    

    def __unicode__(self):
        return str(self.image)