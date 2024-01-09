from django.urls import path
from . import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('todolist/', views.todolist, name='todolist'),
    path('deleteitem/<int:todoID>', views.deleteitem, name='deletetodo')
]
