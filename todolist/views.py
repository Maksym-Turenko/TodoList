from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from todolist.models import Task, Tag
from todolist.forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    template_name = "todo/home.html"
    context_object_name = "tasks"
    ordering = ["is_done", "-created_at"]


class TagListView(ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/add_task.html"
    success_url = reverse_lazy("home")


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/add_tag.html"
    success_url = reverse_lazy("tag_list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/add_task.html"
    success_url = reverse_lazy("home")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/add_tag.html"
    success_url = reverse_lazy("tag_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/delete_confirm.html"
    success_url = reverse_lazy("home")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo/delete_confirm.html"
    success_url = reverse_lazy("tag_list")


def toggle_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = not task.is_done
    task.save()
    return redirect("home")
