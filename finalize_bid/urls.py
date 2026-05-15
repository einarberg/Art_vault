from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='finalize-bid-index'),
    path('bids/<int:id>/', views.index, name='get_bids'),
]
