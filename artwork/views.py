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
from django.shortcuts import get_object_or_404


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

