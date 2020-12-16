from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import *
from django.core.exceptions import ValidationError

class registerform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ''}), label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': ''}), label="Confirm Password")

    def clean_password(self):
        print (self.cleaned_data)
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_verify')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError(_('Your passwords do not match'), code='invalid') 
        return password2

    class Meta:
        model = Account
        fields = ['enrollment','first_name','last_name','Email','password','confirm_password']


class Subjectup(forms.ModelForm):
    class Meta:
        model = SubjectUpload
        fields =['classname','subject','filename','video']