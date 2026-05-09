from django.core.signals import request_started
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "finalize_bid/finalize_bid.html", {
        "artwork": None
    })