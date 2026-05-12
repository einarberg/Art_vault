from django.core.signals import request_started
from django.http import HttpResponse
from django.shortcuts import render
from artwork.models import Artwork


def get_all_artworks(request):
    artworks = Artwork.objects.filter(active=True)
    return render(request, "artwork/all_artworks.html", {"artwork": artworks})

def homepage(request):
    artworks = Artwork.objects.filter(active=True)
    return render(request, "artwork/homepage.html", {"artwork": artworks})
    
def get_artwork_by_id(request, artwork_id):
    artwork = get_object_or_404(artwork, id=artwork_id)
    return render(request, "artwork/artwork.html", {"artwork": artwork_info})
