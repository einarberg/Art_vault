from django import forms
from user.models import User
from django.contrib.auth.forms import UserCreationForm


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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'bio', 'profile_image']

