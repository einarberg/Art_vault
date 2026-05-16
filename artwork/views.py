from operator import truediv

from django.core.signals import request_started
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from psycopg2.extensions import JSON
from django.utils.timezone import now
from datetime import timedelta

import artwork
from user.models import User
from artwork.models import Artwork
from artwork.models import Style
from finalize_bid.models import Bid
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from artwork.forms import ContactForm, PaymentForm

FINALIZE_STEPS = ['contact', 'payment', 'review', 'confirmation']

def get_session_data(request, bid_id):
    return request.session.get(f'finalize_{bid_id}', {})

def save_session_data(request, bid_id, data):
    key = f'finalize_{bid_id}'
    session_data = request.session.get(key, {})
    session_data.update(data)
    request.session[key] = session_data
    request.session.modified = True

@login_required
def finalize_bid(request, bid_id):
    return redirect('finalize_step', bid_id=bid_id, step='contact')

@login_required
def finalize_step(request, bid_id, step):
    bid = get_object_or_404(Bid, id=bid_id, bidder=request.user, accepted=True)

    if step not in FINALIZE_STEPS or step == 'confirmation':
        return redirect('finalize_step', bid_id=bid_id, step='contact')

    session_data = get_session_data(request, bid_id)

    #contact step
    if step == 'contact':
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                save_session_data(request, bid_id, {'contact': form.cleaned_data})
                return redirect('finalize_step', bid_id=bid_id, step='payment')

        else:
            initial = session_data.get('contact', {})
            form = ContactForm(initial=initial)
        return render(request, 'finalize_bid/contact.html', {
            'form': form, 'bid': bid, 'step': step, 'steps': FINALIZE_STEPS
        })

    #payment step
    if step == 'payment':
        if request.method == 'POST':
            form = PaymentForm(request.POST)
            if form.is_valid():
                save_session_data(request, bid_id, {'payment': form.cleaned_data})
                return redirect('finalize_step', bid_id=bid_id, step='review')
        else:
            initial = session_data.get('payment', {})
            form = PaymentForm(initial=initial)
        return render(request, 'finalize_bid/payment.html', {
            'form': form, 'bid': bid, 'step': step, 'steps': FINALIZE_STEPS
        })

    #review step
    if step == 'review':
        contact = session_data.get('contact')
        payment = session_data.get('payment')

        if not contact or payment:
            messages.warning(request, "Please complete all steps before reviewing.")
            return redirect('finalize_step', bid_id=bid_id, step='contact')

        if request.method == 'POST':
            #mark bid as finalized
            bid.finalized = True
            bid.save()
            request.session.pop(f'finalize_{bid_id}', None)
            return redirect('finalize_confirmation', bid_id=bid_id)

        return render(request, 'artwork/finalize/review.html', {
            'bid': bid, 'contact': contact, 'payment': payment, 'step': step, 'steps': FINALIZE_STEPS
        })

@login_required
def finalize_confirmation(request, bid_id):
    bid = get_object_or_404(Bid, id=bid_id, bidder=request.user)
    return render(request, 'artwork/finalze/confirmation.html', {'bid': bid})

def homepage(request):

    search_filter = request.GET.get('search_filter')

    if search_filter is not None:

        artworks = (
            Artwork.objects
            .filter(title__icontains=search_filter)
            .select_related('artist')
            .order_by('title')
        )

        return JsonResponse({
            'data': [
                {
                    'id': x.id,
                    'thumbnail': str(x.thumbnail) if x.thumbnail else None,
                    'title': x.title,
                    'artist': x.artist.seller.user.name,
                }
                for x in artworks
            ]
        })

    artworks = Artwork.objects.all()
    return render(request, "artwork/homepage.html", {"artwork": artworks})


def all_artworks(request):
    artworks = Artwork.objects.all()
    return render(request, "artwork/all_artworks.html", {"artworks": artworks})


def all_artists(request):
    artists = User.objects.filter(seller__artist__isnull=False)
    return render(request, 'artwork/all_artist.html', {'artists':artists})


def artist_artworks(request, id):
    artworks = Artwork.objects.filter(artist__seller__user__id=id)
    return render(request, 'artwork/artist.html', {'artworks': artwork})


def get_artwork_by_id(request, id):
    artwork = get_object_or_404(Artwork, id=id)
    style = get_object_or_404(Style, id=artwork.style_id)
    min_bid = artwork.bid_price + 1
    if request.method == "POST":
        bid_amount = request.POST.get("bid_amount")
        
        Bid.objects.create(
            artwork = artwork,
            buyer = request.user.buyer,
            price = bid_amount,
            expiration_date = now() + timedelta(days=30),
            status = "pending",
        )
        
        artwork.bid_status = "Bidding"
        artwork.bid_price = bid_amount
        artwork.save()

    return render(request, "artwork/artwork.html", {"artwork": artwork, "style": style, "min_bid": min_bid})

