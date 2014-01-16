from .models import Blog, BlogSearch

from django.db.models import Q

STRIP_WORDS = ['a','an','by','for','from','in','no','not','of','on','or','that','the','to','with']


#store the search text in the database

def store(request, q, matched_blogs):
    #if search term is at least three chars long, store in db
    if len(q) >2:
        for blog in matched_blogs:
            term = BlogSearch()
            term.q = q
            term.blog = blog
            term.ip_address = request.META.get('REMOTE_ADDR')
            term.user = None
            if request.user.is_authenticated():
                term.user = request.user
            term.save()
        

# get blogs matching the search text
def blogs(search_text):
    words = _prepare_words(search_text)
    blogs = Blog.active.all()
    results = {}
    results['blogs'] = []
    #iterate through keywords
    for word in words:
        blogs = blogs.filter(Q(title__icontains=word) |
        Q(sub_title__icontains=word) |
        Q(meta_keywords__icontains=word) |
        Q(meta_description__icontains=word))
        results['blogs'] = blogs
    return results

# strip ou common words, limit to 5 words
def _prepare_words(search_text):
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
        return words[0:5]