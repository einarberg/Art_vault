from django import forms
from user.models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username'
        })

        self.fields['password1'].widget.attrs.update({
            'placeholder': 'Enter password'
        })

        self.fields['password2'].widget.attrs.update({
            'placeholder': 'Confirm password'
        })


class CustomAuthenticationForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'placeholder': 'Enter username'
        })

        self.fields['password'].widget.attrs.update({
            'placeholder': 'Enter password'
        })

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'bio', 'profile_image']

