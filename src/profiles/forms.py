from django import forms

from .models import Profile, UserPicture


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        
        
class UserPictureForm(forms.ModelForm):
    class Meta:
        model = UserPicture