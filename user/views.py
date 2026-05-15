from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from user.models import User


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        return render(request, 'Users/register.html', {
            'form': UserCreationForm()
        })


def profile(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, 'Users/Profile.html', {"user": user})


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)

    return render(request, 'Users/Profile_edit.html', {'form': form})
