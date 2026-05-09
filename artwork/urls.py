from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('all_artworks/', views.all_artworks, name='all-artworks'),
    path('<int:id>', views.get_artwork_by_id, name='artwork-by-id'),
]