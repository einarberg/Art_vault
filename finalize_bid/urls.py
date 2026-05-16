from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='finalize-bid-index'),
    path('payment/', views.payment, name='finalize-bid-payment'),
    path('payment/credit/', views.payment, name='credit-card'),
    path('bids/<int:id>/', views.get_bids, name='get_bids'),
    path('review/', views.review, name='finalize-bid-review'),
    path('success/', views.success, name='finalize-bid-success'),
]
