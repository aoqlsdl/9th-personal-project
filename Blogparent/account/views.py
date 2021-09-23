from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from account.forms import RegisterForm,CustomUserChangeForm

from .models import AbstractUser
# Create your views here.

def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
        return redirect('home')
    else:
        form = RegisterForm()
        return render(request, 'signup.html',{'form':form})

def edit_user_info(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=request.user)
        context = {
            'form': form
        }
    return render(request, 'edit_user_info.html', context)