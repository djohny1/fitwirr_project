from django import forms
from .models import BlogSearch

class BlogSearchForm(forms.ModelForm):
    class Meta:
        model = BlogSearch
        
    def __init__(self, *args, **kwargs):
        super(BlogSearchForm, self).__init__(*args, **kwargs)
        default_text = 'Search'
        self.fields['q'].widget.attrs['value'] = default_text
        self.fields['q'].widget.attrs['onfocus'] = "if (this.value=='" + default_text + "')this.value = ''"
    inlude = ('q',)
        
