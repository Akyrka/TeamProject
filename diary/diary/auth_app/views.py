from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("tasks:list")  # редірект на список задач
    else:
        form = UserCreationForm()
    return render(request, 'auth_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect("tasks:list")
    else:
        form = AuthenticationForm()
    return render(request, 'auth_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')


