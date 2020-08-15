from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class Forms(forms.Form):
    task = forms.CharField(label="New task")


def index(request):
    if "tasks" not in request.session:
        request.session['tasks'] = []
    context = {
        "tasks": request.session['tasks'],
        "form": Forms()
    }
    return render(request, "tasks/index.html", context)

def add(request):
    if request.method == "POST":
        form = Forms(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            request.session['tasks'] += [task]
    return HttpResponseRedirect(reverse('index'))


def removetask(request):
    tasks = request.session['tasks']
    index = int(request.GET.get('id'))
    del tasks[index]
    request.session['tasks'] = tasks
    return HttpResponseRedirect(reverse('index'))


def inc(request, index):
    tasks = request.session['tasks']
    if index > 0:
        task = tasks[index]
        prevtask = tasks[index - 1]
        tasks[index] = prevtask
        tasks[index - 1] = task
        request.session['tasks'] = tasks
    return HttpResponseRedirect(reverse("index"))


def dec(request, index):
    tasks = request.session['tasks']
    if index < len(tasks) - 1:
        task = tasks[index]
        prevtask = tasks[index + 1]
        tasks[index] = prevtask
        tasks[index + 1] = task
        request.session['tasks'] = tasks
    return HttpResponseRedirect(reverse("index"))
