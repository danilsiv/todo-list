from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views import generic

from planner.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "planner/task_list.html"
    context_object_name = "task_list"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = "planner:task-list"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = "planner:task-list"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("planner:task-list")


def change_status(request: HttpRequest, pk: int) -> HttpResponse:
    task = Task.objects.get(id=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("planner:task-list")

