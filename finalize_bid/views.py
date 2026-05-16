from django.core.signals import request_started
from django.http import HttpResponse
from django.shortcuts import render, redirect

from finalize_bid.models import Bid


# Create your views here.

def index(request):

    if request.method == "POST":

        request.session["contact"] ={
            "street": request.POST.get("street"),
            "city": request.POST.get("city"),
            "postal_code": request.POST.get("postal_code"),
            "national_id": request.POST.get("national_id"),
            "country": request.POST.get("country"),
        }

        return redirect("finalize-bid-payment")

    return render(request, "finalize_bid/finalize_bid.html")
def payment(request):

    if request.method == "POST":

        payment_type = request.POST.get("payment_type")

        request.session["payment"] = {
            "payment_type": payment_type,
            "cardholder_name": request.POST.get("cardholder_name"),
            "card_number": request.POST.get("card_number"),
            "cvc": request.POST.get("cvc"),

            "bank_account": request.POST.get("bank_account"),

            "bank_name": request.POST.get("bank_name"),
            "routing_number": request.POST.get("routing_number"),
            "account_number": request.POST.get("account_number"),
        }

        return redirect("finalize-bid-review")

    return render(request, "finalize_bid/finalize_bid_payment.html")

def review(request):
    contact = request.session.get("contact", {})
    payment = request.session.get("payment", {})

    if request.method == "POST":
        return redirect("finalize-bid-success")

    return render(request, "finalize_bid/finalize_bid_review.html", {
        "contact": contact,
        "payment": payment
    })

def success(request):

    contact = request.session.get("contact", {})
    payment = request.session.get("payment", {})

    return render(request, "finalize_bid/finalize_bid_success.html", {
        "contact": contact,
        "payment": payment
    })



def get_bids(request, id):
    bids = Bid.objects.filter(buyer__user__id=id)
    return render(request, "finalize_bid/bids.html", {"bids": bids})
