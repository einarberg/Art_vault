from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='finalize-bid-index'),
    path('payment/', views.payment, name='finalize-bid-payment'),
    path('payment/credit/', views.payment, name='credit-card'),
    path('payment/bank/', views.bank_transfer, name='bank-transfer'),
    path('payment/wire/', views.wire_transfer, name='wire-transfer'),
    path('bids/<int:id>/', views.index, name='get_bids'),
    path('review/', views.review, name='finalize-bid-review'),
]
