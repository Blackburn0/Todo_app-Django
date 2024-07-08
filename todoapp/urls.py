from django.urls import path
from .views import HomeView, todo_list, TodoCreateView, TodoUpdateView, TodoDeleteView, TodoDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dashboard/', todo_list, name='todo-list'),
    path('dashboard/todo/create/', TodoCreateView.as_view(), name='create-todo'),
    path('dashboard/todo/detail/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('dashboard/todo/delete/<int:pk>/', TodoDeleteView.as_view(), name='delete-todo'),
    path('dashboard/todo/update/<int:pk>/', TodoUpdateView.as_view(), name='update-todo'),
]
