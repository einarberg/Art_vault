from user.forms import ProfileForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from user.models import UserProfile
from artwork.models import Artwork
from user.forms import CustomUserCreationForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        print(form.errors)

        if form.is_valid():
            auth_user =form.save()

            UserProfile.objects.create(
                auth_user=auth_user,
                name=auth_user.username,
                email=auth_user.email
            )

            return redirect('login')
    else:
        form = CustomUserCreationForm()

    # Reload page with form + errors
    return render(request, 'Users/register.html', {
        'form': form
    })


def profile(request, id):
    user = get_object_or_404(UserProfile, id=id)
    return render(request, 'Users/Profile.html', {"user": user})


def seller_profile(request, id):
    user = get_object_or_404(UserProfile, id=id)
    artworks = Artwork.objects.filter(seller__user__id=id)
    return render(request, 'Users/Seller_profile.html', {"user": user, "artworks": artworks})


def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'Users/Profile_edit.html', {'form': form})

