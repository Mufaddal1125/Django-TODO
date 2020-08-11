from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class Forms(forms.Form):
    task = forms.CharField(label="New task")


def index(request):
    if "tasks" not in request.session or "priority" not in request.session:
        request.session['tasks'] = []
        request.session['priority'] = 0
    context = {
        "tasks": request.session['tasks'],
        "form": Forms()
    }
    return render(request, "tasks/index.html", context)


def taskssort(e):
    return e['priority']


def add(request):
    if request.method == "POST":
        form = Forms(request.POST)
        if form.is_valid():
            request.session['priority'] = len(request.session['tasks']) + 1
            task = {"task": form.cleaned_data['task'], "priority": request.session['priority']}
            request.session['tasks'] += [task]
            request.session['tasks'].sort(key=taskssort)

    return HttpResponseRedirect(reverse('index'))

def removetask(request):
    tasks = request.session['tasks']
    index = int(request.GET.get('id'))
    del tasks[index]
    request.session['tasks'] = tasks
    return HttpResponseRedirect(reverse('index'))


def inc(request, index):
    tasks = request.session['tasks']
    tasks[index]["priority"] -= 1
    request.session['tasks'] = tasks
    request.session['tasks'].sort(key=taskssort)
    return HttpResponseRedirect(reverse("index"))


def dec(request, index):
    tasks = request.session['tasks']
    tasks[index]["priority"] += 1
    request.session['tasks'] = tasks
    request.session['tasks'].sort(key=taskssort)
    return HttpResponseRedirect(reverse("index"))
