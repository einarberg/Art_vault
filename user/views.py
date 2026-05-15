from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
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

def profile(request):
    return render(request, 'Users/Profile.html')


def edit_profile(request):
    return render(request, 'Users/Profile/Edit.html')

