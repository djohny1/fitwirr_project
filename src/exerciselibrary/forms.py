from django.forms import ModelForm
from .models import Exercise, ExerciseImage


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = ('title', 'description', 'muscle', 'level','home_gym','active',)
        
        
        
class ExerciseImageForm(ModelForm):
    class Meta:
        model = ExerciseImage
        
        
        