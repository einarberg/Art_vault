from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from user.forms import CustomAuthenticationForm

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='Users/login.html', authentication_form=CustomAuthenticationForm), name='login'),
    path('logout/', LogoutView.as_view(next_page='homepage'), name='logout'),
    path('profile/<int:id>/', views.profile, name='profile'),
    path('seller_profile/<int:id>/', views.seller_profile, name='seller_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
