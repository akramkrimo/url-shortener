from django.shortcuts import render, redirect, reverse
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, authenticate, login, logout
# Create your views here.



User = get_user_model()
def register(request):
    if request.user.is_authenticated:
        return redirect('shortener:shortener')
        
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username, email, password)
            return redirect('accounts:login')
    form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('shortener:shortener')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password )
            login(request, user)
            return redirect('shortener:shortener')
    form = LoginForm()
    return render(request, 'accounts/index.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')