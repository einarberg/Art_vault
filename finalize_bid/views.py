from django.core.signals import request_started
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "finalize_bid/finalize_bid.html", {
        "artwork": None
    })
def payment(request):
    return render(request, "finalize_bid/finalize_bid_payment.html")

def bank_transfer(request):
    return render(request, "finalize_bid/finalize_bid_bank.html")

def wire_transfer(request):
    return render(request, "finalize_bid/finalize_bid_wire.html")

def get_bids(request, id):
    bids = Bid.objects.filter(buyer__user__id=id)
    return render(request, "finalize_bid/bids.html", {"bids": bids})

def review(request):
    return render(request, "finalize_bid/finalize_bid_review.html")
