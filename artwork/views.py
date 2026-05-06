from django.core.signals import request_started
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

artwork = [
    {
        "id":1,
        'title': 'title',
    }
]



def index(request):
    return render(request, "artwork/all_artworks.html", {
        "artworks": artwork
    })


def get_artwork_by_id(request, id):
    return HttpResponse(f"Response from {request.path} with id {id}")