from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [

path('get_todos', views.get_post_todos, name='get_post_todos'),


]