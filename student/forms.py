from django import forms
from .models import *

class uploadform(forms.ModelForm):
    class Meta:
        model = stupload
        fields = ['classname','filename','submission']


class linkform(forms.ModelForm):
    class Meta:
        model = links
        fields = ['classname', 'link']