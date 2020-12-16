from django.urls import path,include, re_path
from . import views

urlpatterns=[
    path('',views.home),
    path('home', views.home),
    path('edit', views.edit),
    path('class', views.clas),
    path('add', views.add),
    path('detain', views.deatin),
    path('promotion', views.promotion),
    path('attendance', views.attendance),
    path('faculty_subject', views.faculty_subject),
    path('prac_class', views.prac_class),
    path('practical_submit', views.practical_submit),
    path('request', views.request),
    path('subject_upload', views.subject_upload),
    path('add_faculty', views.add_faculty),
    path('add_student', views.add_student),
    path('allocate', views.allocate),
    path('remove_faculty', views.remove_faculty),
    path('remove_student', views.remove_student),
    re_path(r'^logout', views.logout),
]