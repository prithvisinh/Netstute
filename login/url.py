from django.urls import path,include,re_path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='Register'),
    path('view', views.view),
    path('login', views.home),
    re_path(r'^logout',views.lout),
    path('forgot',views.forgot, name='forgot'),
]