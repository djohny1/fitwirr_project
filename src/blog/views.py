import time
from calendar import month_name

from django.views.generic.list import ListView

from django.shortcuts import render_to_response, get_object_or_404
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog, Category, BlogImage
from .search import blogs as search_blogs, store as search_store


def index(request):
    
    #blog = Blog.objects.filter(active=True).order_by('-id')
    blog = Blog.objects.all().order_by('-id')
    categories = Category.objects.all()
    pub_date = Blog.objects.all().order_by('-id')[:6]
    
    paginator = Paginator(blog, 10)
    
    page = request.GET.get('page')
    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        
        blog = paginator.page(paginator.num_pages)
        
    return render_to_response('blog/index.html', locals(), context_instance=RequestContext(request))
    
    
def view_post(request, slug):
    blog = Blog.objects.get(slug=slug)
    #pub_date = Blog.objects.filter(is_active=True)
    pub_date = Blog.objects.all().order_by('-id')[:6]
   
    images = blog.blogimage_set.all()
    
    categories = Category.objects.all()
  
  
  
    return render_to_response('blog/view_post.html', locals(), context_instance=RequestContext(request))


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/view_category.html',{
    'category': category,
    'posts' : Blog.objects.filter(category=category)[:6]
   })


def tagpage(request, tag):
    blog = Blog.objects.filter(tags__name=tag)
    return render_to_response('blog/tagpage.html', locals(), context_instance=RequestContext(request))

def search(request):
    # get the current search phrase
    q = request.GET.get('q', '')
    try:
        blogs = search_blogs(q).get('blogs')
        search_store(request, q, blogs)
    except ValueError, e:
        print e

    page_title = 'Search Results for: ' + q


    paginator = Paginator(blogs, 10)
    
    page = request.GET.get('page')
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        
        blogs = paginator.page(paginator.num_pages)
    
    return render_to_response('blog/search_results.html',locals(), context_instance=RequestContext(request))
