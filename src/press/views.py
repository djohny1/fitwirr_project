from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect, get_object_or_404# Create your views here.
from django.http import HttpResponse

from django.views.generic.list import ListView
from .models import News, NewsImage

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def press_room(request):
    news_realease = News.objects.all().order_by('-pub_date')[:5]
    
    return render_to_response("press/press_room.html", locals(), context_instance=RequestContext(request))



def view_news(request, slug):
    #news = News.objects.all().order_by('-id')
    news = News.objects.filter(slug=slug)
    #image = news.news_image_set.all()
    
    #latest_press_realease = News.objects.all().order_by('-pub_date')[:5]
    
    return render_to_response("press/view_news.html", locals(), context_instance=RequestContext(request))







def list(request):
    """
    Returns a list of press releases
    """
    all_news = News.objects.all().order_by('-id')
    
   
    
    paginator = Paginator(all_news, 10)
    
    
    page = request.GET.get('page')
    try:
        all_news = paginator.page(page)
    except PageNotAnInteger:
        all_news = paginator.page(1)
    except EmptyPage:
        
        all_news = paginator.page(paginator.num_pages)
        

    
    return render_to_response("press/list.html", locals(), context_instance=RequestContext(request))
    
    
    
def logo(request):
   
    return render_to_response("press/logo.html", locals(), context_instance=RequestContext(request))

    
def app_icon(request):
   
    return render_to_response("press/app_icon.html", locals(), context_instance=RequestContext(request))



