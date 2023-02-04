from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.index, name = 'index'),
    path('get-todo-list', views.get_todo_list, name = 'get_todo_list'),
    path('edit-todo-list/<str:pk>/', views.manage_todo_list),
    path('add-todo-list/', views.manage_todo_list),
    path('change-status-todo/<str:pk>/', views.change_status),
]