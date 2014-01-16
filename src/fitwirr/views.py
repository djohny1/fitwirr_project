import re

from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

#from .models import Blog, Category, BlogImage


def search(request):
    search_from_pages  = ('/exerciselibrary','/blog')

    # get the current search phrase
    q = request.GET.get('q', '')
    r = request.GET.get('r', '')
    
    print q
    print r
    
    if r == '/': # if search from Home page
        r = '/exerciselibrary'
        
    match_result = None
    for page in search_from_pages:
        match_result = re.search(page, r)
        
        if match_result is not None:
            break
    
    if match_result is not None:
        from_page = match_result.group()

        #print from_page

        if from_page == '/exerciselibrary':
        #redirect to exerciselibrary search result page
            return HttpResponseRedirect("%s?q=%s" % (reverse('exerciselibrary_search'), q))

        elif from_page == '/blog':
        #redirect to blog search result page
        #return blog_search(request)
            return HttpResponseRedirect("%s?q=%s" % (reverse('blog_search'), q))
    
    return HttpResponseRedirect("%s?q=%s" % (reverse('exerciselibrary_search'), q))
