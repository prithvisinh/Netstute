from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from login.models import *


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)


    class Meta:
        model = Account
        fields = ('enrollment' ,'first_name', 'last_name','Email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('enrollment' ,'first_name', 'last_name','Email', 'is_active', 'is_admin', 'is_Faculty', 'is_HOD')

    def clean_password(self):
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('enrollment' ,'is_HOD', 'is_Faculty')
    list_filter = ('is_HOD',)
    fieldsets = (
        (None, {'fields': ('enrollment' ,'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name','Email')}),
        ('Permissions', {'fields': ('is_HOD', 'is_Faculty',)}),
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
            	 'enrollment' ,
            	 'first_name',
            	  'last_name',
                    'Email',
            	   'is_active',
            	    'is_Faculty',
            	     'is_HOD',
            	      'password1',
            	       'password2'
            	           ),
        }),
    )
    search_fields = ('enrollment',)
    ordering = ('enrollment',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(Account, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)

class FieldAdmin(admin.ModelAdmin):
	list_display=['field','course']

class subjectlist(admin.ModelAdmin):
    list_display = ['Subject','shortname','field']

class ClassAdmin(admin.ModelAdmin):
    list_display =['classname','field','faculty']

class studentAdmin(admin.ModelAdmin):
	list_display = ['Enrollment','field']

class upload(admin.ModelAdmin):
    list_display = ['classname','subject','filename']

class FacultyAdmin(admin.ModelAdmin):
	list_display=['Enrollment', 'field','is_HOD']

admin.site.register(SubjectUpload,upload)
admin.site.register(Faculty,FacultyAdmin)
admin.site.register(Student,studentAdmin)
admin.site.register(Field,FieldAdmin)
admin.site.register(subjectList,subjectlist)
admin.site.register(Classroom,ClassAdmin)