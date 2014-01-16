from django.shortcuts import render_to_response, RequestContext, Http404, get_object_or_404, HttpResponseRedirect

from django.template.defaultfilters import slugify
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import login_required


from .models import Exercise, Category, ExerciseImage, CategoryImage
from .forms import ExerciseForm, ExerciseImageForm
from .search import exercises as search_exercises, store as search_store
from taggit.models import Tag


def list_all(request):
    exercises = Exercise.objects.filter(active=True).order_by('?')
    page_tile = 'Exercises and workouts plan for weight loss for getting fit'
   
    
    return render_to_response("exercise_library/all.html", locals(), context_instance=RequestContext(request))


def fitwirr(request):
    
    return render_to_response("exercise_library/fitwirr.html", locals(), context_instance=RequestContext(request))


def about(request):
    
    return render_to_response("exercise_library/about.html", locals(), context_instance=RequestContext(request))






@login_required
def add_exercise(request):
    form = ExerciseForm(request.POST or None)
    
    if form.is_valid():
        exercise = form.save(commit=False)
        exercise.user = request.user
        exercise.slug = slugify(form.cleaned_data['title'])
        exercise.active = False
        exercise.save()
        return HttpResponseRedirect(reverse('single_exercise', kwargs={'slug':exercise.slug}))
    
    
    return render_to_response("exercise_library/edit.html", locals(), context_instance=RequestContext(request))

@login_required
def manage_exercise_image(request, slug):
    try:
        exercise = Exercise.objects.get(slug=slug)
    except:
        exercise = False
        
    if request.user == exercise.user:
        queryset=ExerciseImage.objects.filter(exercise__slug=slug)
        ExerciseImageFormset = modelformset_factory(ExerciseImage, form=ExerciseImageForm)
        formset = ExerciseImageFormset(request.POST or None, request.FILES or None, queryset=queryset)
        form = ExerciseImageForm(request.POST or None)
        
        if formset.is_valid():
           for form in formset:
                instance = form.save(commit=False)
                instance.save()
        return render_to_response("exercise_library/image_images.html", locals(), context_instance=RequestContext(request))
    else:
        raise Http404
    



@login_required
def edit_exercise(request, slug):
    instance = Exercise.objects.get(slug=slug)
    if request.user == request.user:
        form = ExerciseForm(request.POST or None, instance=instance)
        
        if form.is_valid():
            exercise.edit = form.save(commit=False)
            exercise.edit.save()
    
        return render_to_response("exercise_library/edit.html", locals(), context_instance=RequestContext(request))
    else:
        raise Http404
    
    

def single(request, slug):
    #exercise = Exercise.objects.get(slug=slug)
    exercise = get_object_or_404(Exercise, slug=slug)
    
    images = exercise.exerciseimage_set.all()
    #categories = exercise.category_set.all()
    category = Category.objects.filter(active=True)
    tags=Tag.objects.all()
    related_exercises = CategoryImage.objects.filter(featured_image=True).order_by('-id')[:3]


    return render_to_response("exercise_library/single.html", locals(), context_instance=RequestContext(request))

def exercise_tagpage(request, tag):
    exercise = Exercise.objects.filter(tags__name=tag)
    return render_to_response('exercise_library/exercise_tagpage.html', locals(), context_instance=RequestContext(request))





def search(request):
    # get the current search phrase
    q = request.GET.get('q', '')
    try:
        exercises = search_exercises(q).get('exercises')
        search_store(request, q, exercises)
    except ValueError, e:
        print e

    page_title = 'Search Results for: ' + q


    return render_to_response('exercise_library/search.html',locals(), context_instance=RequestContext(request))



@login_required
def like_or_dislike_exercise_image(request, image_id):
    """
    Ajax function to like or dislike an exercise image
    """
    if request.is_ajax():
        images = None
        try:
            images = ExerciseImage.objects.filter(pk=image_id)
        except Exceptionn, e:
            pass
            
        if len(images) > 0:
            image = images[0]
            
            action, like_count = ExerciseImage.objects.like_or_dislike_exercise_image(request.user, image)
            
        else:
            image = None
            
        context = {
            'image' : image, 
            'user' : request.user,
            'action' : action,
            'like_count' : like_count

        }
        #print request.user
        return render_to_response('exercise_library/_include_image_like_buttons.html',context,context_instance=RequestContext(request))
    else:
        raise Http404   
    
     

