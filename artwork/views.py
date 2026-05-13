from django.core.signals import request_started
from django.http import HttpResponse
from django.shortcuts import render
from artwork.models import Artwork
from artwork.models import Style
from django.shortcuts import get_object_or_404


def all_artworks(request):
    artworks = Artwork.objects.all()
    return render(request, "artwork/all_artworks.html", {"artworks": artworks})

def homepage(request):
    artworks = Artwork.objects.all()
    return render(request, "artwork/homepage.html", {"artwork": artworks})
    
def get_artwork_by_id(request, id):
    artwork = get_object_or_404(Artwork, id=id)
    style = get_object_or_404(Style, id=artwork.style_id)
    return render(request, "artwork/artwork.html", {"artwork": artwork, "style": style})
