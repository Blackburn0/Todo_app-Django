from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Todo
from django.urls import reverse_lazy


# Create your views here.

class HomeView(TemplateView):
    template_name = 'todoapp/index.html'


class TodoListView(ListView):
    model = Todo

class TodoDetailView(DetailView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy('todo-list')


class TodoUpdateView(UpdateView):
    model = Todo
    fields = "__all__"
    success_url = reverse_lazy('todo-list')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')
