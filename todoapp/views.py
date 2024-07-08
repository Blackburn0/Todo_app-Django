from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView, DetailView
from .models import Todo
from django.urls import reverse_lazy
from django.shortcuts import render

# Create your views here.

class HomeView(TemplateView):
    template_name = 'todoapp/index.html'


def todo_list(request):
    todo =Todo.objects.filter(owner=request.user)
    context = {
        'todo': todo
    }
    return render(request, 'todoapp/todo_list.html', context)

    
class TodoDetailView(DetailView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ['name', 'task']
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user 
        return super().form_valid(form)


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['name', 'task']
    success_url = reverse_lazy('todo-list')


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')
