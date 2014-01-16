from .models import Exercise, ExerciseSearch

from django.db.models import Q

STRIP_WORDS = ['a','an','by','for','from','in','no','not','of','on','or','that','the','to','with']


#store the search text in the database

def store(request, q, matched_exercises):
    #if search term is at least three chars long, store in db
    if len(q) >2:
        for exercise in matched_exercises:
            term = ExerciseSearch()
            term.q = q
            term.exercise = exercise
            term.ip_address = request.META.get('REMOTE_ADDR')
            term.user = None
            if request.user.is_authenticated():
                term.user = request.user
            term.save()
        

# get blogs matching the search text
def exercises(search_text):
    words = _prepare_words(search_text)
    exercises = Exercise.active_objects.all()
    results = {}
    results['exercises'] = []
    #iterate through keywords
    for word in words:
        exercises = exercises.filter(Q(title__icontains=word) |
        Q(meta_keywords__icontains=word) |
        Q(meta_description__icontains=word) |
        Q(category__active=True, category__meta_keywords__icontains=word) |
        Q(category__active=True, category__meta_description__icontains=word))
        
        results['exercises'] = exercises
    return results

# strip ou common words, limit to 5 words
def _prepare_words(search_text):
    words = search_text.split()
    for common in STRIP_WORDS:
        if common in words:
            words.remove(common)
        return words[0:5]