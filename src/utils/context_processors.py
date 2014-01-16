from blog.models import Category
from exerciselibrary.models import Category

from fitwirr import settings

def fitwirr(request):
    return {
          'active_categories': Category.objects.filter(active=True),
          'site_name': settings.SITE_NAME,
          'meta_keywords': settings.META_KEYWORDS,
          'meta_description': settings.META_DESCRIPTION,
          'request': request
    
    }