from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('home', views.home),
    path('edit', views.edit),
    path('attendance', views.attendance),
    path('chat', views.chat),
    path('practical', views.practical),
    path('request', views.request),
    path('student_subject', views.student_subject),
    path('subject_class', views.subject_class),
    re_path(r'^logout', views.view_logout),
]