from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [

path('', views.get_post_todos, name='get_post_todos'),
path('get_todos_update/<int:pk>/', views.get_delete_update_todos, name='get_delete_update_todos'),

]