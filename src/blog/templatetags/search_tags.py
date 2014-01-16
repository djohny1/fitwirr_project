from django import template

from blog.forms import BlogSearchForm
import urllib

register = template.Library()

@register.inclusion_tag('blog/search_box.html')
def search_box(request):
    q = request.GET.get('q','')
    form = BlogSearchForm({'q': q })
    return {'form': form }
 
 