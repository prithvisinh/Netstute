from django.contrib import admin
from .models import *

class Timetable(admin.ModelAdmin):
    list_display = ['Enrollment','field','timetable']


class Timetable_student(admin.ModelAdmin):
    list_display = ['Field']


admin.site.register(timetableHOD, Timetable)
admin.site.register(timetableStudent,Timetable_student)