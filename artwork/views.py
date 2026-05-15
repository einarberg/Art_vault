from django.core.signals import request_started
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from psycopg2.extensions import JSON

import artwork
from artwork.models import Artwork
from artwork.models import Style
from django.shortcuts import get_object_or_404


def homepage(request):
    if 'search_filter' in request.GET:
        return JsonResponse({
            'data': [{
                'id': x.id,
                'thumbnail': str(x.thumbnail) if x.thumbnail else None,
                'title': x.title,
                'artist': x.artist.seller.user.name,
            } for x in Artwork.objects.filter(title__icontains=request.GET['search_filter']).order_by('title')]
        })

    artworks = Artwork.objects.all()
    return render(request, "artwork/homepage.html", {"artwork": artworks})


def all_artworks(request):
    artworks = Artwork.objects.all()
    return render(request, "artwork/all_artworks.html", {"artworks": artworks})


def all_artists(request):
    artworks = Artwork.objects.all()
    return render(request, "artwork/all_artist.html", {"artworks": artworks})


def get_artwork_by_id(request, id):
    artwork = get_object_or_404(Artwork, id=id)
    style = get_object_or_404(Style, id=artwork.style_id)
    return render(request, "artwork/artwork.html", {"artwork": artwork, "style": style})

