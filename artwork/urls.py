from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('all_artworks/', views.all_artworks, name='all-artworks'),
    path('all_artist/', views.all_artists, name='all-artists'),
    path('artist/<int:id>', views.artist_artworks, name='artist-artworks'),
    path('<int:id>', views.get_artwork_by_id, name='artwork-by-id'),

    path('bid/<int:bid_id>/finalize/', views.finalize_bid, name='finalize_bid'),
    path('bid/<int:bid_id>/finalize/<str:step>/', views.finalize_step, name='finalize_step'),
    path('bid/<int:bid_id>/finalize/done/', views.finalize_confirmation, name='finalize_confirmation'),
]
