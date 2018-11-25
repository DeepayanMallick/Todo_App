from django.urls import path
from . import views  
urlpatterns = [
    path('', views.index, name='index'),
    path('todo/<int:todo_id>/', views.todo_detail, name='todo_detail'),
    path('todo/<int:todo_id>/update/', views.update_todo, name='update_todo'),
    path('todo/', views.create_todo, name='create_todo'),
]