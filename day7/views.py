from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseForbidden
from django.urls import reverse
from django.contrib import messages
from . import forms
from . import models

@login_required
def index(request):
    tasks = models.Task.objects.filter(user=request.user)
    if request.method == "POST":
        add_task_form_data = forms.AddTaskForm(data=request.POST)
        if add_task_form_data.is_valid():
            cleaned_data = add_task_form_data.cleaned_data
            models.Task.objects.create(
                user=request.user,
                title=cleaned_data.get('title'),
                desc=cleaned_data.get('desc'),
                deadline=cleaned_data.get('deadline')
            )
            return redirect("day7:index")
        else:
            return HttpResponse("Invalid Form Data")
    else:
        context = {
            'user': request.user,
            'add_task_form': forms.AddTaskForm,
            'tasks': tasks[::-1],
        }
        return render(request, 'day7/index.html', context)

def register(request):
    if request.method == "POST":
        u_form = forms.UserRegisterForm(request.POST)
        if u_form.is_valid():
            password = u_form.cleaned_data['password']
            users = u_form.save()
            users.set_password(password)
            users.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect(reverse('day7:login_view'))
    else:
        u_form = forms.UserRegisterForm()
    return render(request, "day7/register.html", {'u_form': u_form})


def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('day7:index')
    else:
        form = forms.LoginForm()
    return render(request, 'day7/login.html', {'login_form': form})

def logout_view(request):
    logout(request)
    return redirect('day7:login_view')

@login_required
def update_task(request, task_id):
    task = get_object_or_404(models.Task, id=task_id)
    if request.user != task.user:
        return HttpResponseForbidden("You are not authorized to update this task.")
    
    if request.method == "POST":
        add_task_form_data = forms.UpdateTaskForm(data=request.POST, instance=task)
        if add_task_form_data.is_valid():
            add_task_form_data.save()
            return redirect('day7:index')
        else:
            return HttpResponse("Invalid Form Data")
    else:
        context = {
            'add_task_form': forms.UpdateTaskForm(instance=task),
        }
        return render(request, 'day7/update.html', context)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(models.Task, id=task_id)
    if task.user != request.user:
        return HttpResponseForbidden("You are not authorized to delete this task.")
    task.delete()
    return redirect('day7:index')

@login_required
def order_by_date(request):
    tasks = models.Task.objects.filter(user=request.user).order_by('deadline')
    context = {
        'tasks': tasks,
        'user': request.user,
        'add_task_form': forms.AddTaskForm,
    }
    return render(request, 'day7/index.html', context)

@login_required
def search(request):
    search_text = request.GET.get('search_text')
    tasks = models.Task.objects.filter(title__icontains=search_text, user=request.user)
    context = {
        'tasks': tasks,
        'user': request.user,
        'add_task_form': forms.AddTaskForm,
    }
    return render(request, 'day7/index.html', context)
