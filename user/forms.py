from django import forms
from user.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'bio', 'profile_image']

