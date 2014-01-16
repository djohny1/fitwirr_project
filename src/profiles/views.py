
from django.contrib import messages
from django.shortcuts import render_to_response, RequestContext, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from django.forms.models import modelformset_factory
from .models import Profile, UserPicture
from .forms import ProfileForm, UserPictureForm
from exerciselibrary.models import UserLikeExerciseImage


def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request))


def all(request):
    if request.user.is_authenticated():
        users = User.objects.filter(is_active=True)
    
        return render_to_response('profiles/all.html', locals(), context_instance=RequestContext(request))
    else:
        return render_to_response('profiles/home.html', locals(), context_instance=RequestContext(request))



def single_user(request, username):
    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
            
            userlikes_count = UserLikeExerciseImage.objects.filter(user=user).count()
    except:
        raise Http404
    
    return render_to_response('profiles/single_user.html', locals(), context_instance=RequestContext(request))


def single_user_likes(request, username):
    try:
        user = User.objects.get(username=username)
        if user.is_active:
            single_user = user
            userlikes_count = UserLikeExerciseImage.objects.filter(user=user).count()
                        
            userlikes = UserLikeExerciseImage.objects.filter(user=user)
            
    except:
        raise Http404
    
    return render_to_response('profiles/single_user.html', locals(), context_instance=RequestContext(request))



def edit_profile(request):
    user = request.user
    user_picture = UserPicture.objects.get(user=user)
    user_picture_form = UserPictureForm(request.POST or None, request.FILES or None,  instance=user_picture)
  
    
    if user_picture_form.is_valid():
        form3 = user_picture_form.save(commit=False)
        form3.save()
        
        messages.success(request, 'Profile details updated.')
    else:
        messages.error(request, 'Profile photo did not update.')
    
        
    return render_to_response('profiles/edit_profile.html', locals(), context_instance=RequestContext(request))



  
 