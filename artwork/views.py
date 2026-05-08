from django.core.signals import request_started
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

artworks = [
    {
        "id":1,
        'title': 'Napoleon Crossing the Alps',
        'artist': 'Jacques-Louis David',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Neoclassicism',
        'dimensions': '221 × 260 cm',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/f/fd/David_-_Napoleon_crossing_the_Alps_-_Malmaison2.jpg',
        'year_of_creation': '1800',
        'provenance': 'Jacques-Louis David; Charles IV of Spain; Napoleon Bonaparte',
        'listing_date': '24-6-2026'
    },
    {
        "id": 2,
        "title": "Divine Right",
        "artist": "John Blanche",
        "edition": "original",
        "medium": "Illustration / mixed media",
        "style": "Dark fantasy",
        "dimensions": "Unknown",
        "thumbnail": 'https://i.redd.it/3f0gp3xsrmx71.jpg',
        "year_of_creation": "1980s",
        "provenance": "Private collection; Games Workshop archives",
        "listing_date": "24-6-2026"
    },
    {
        "id": 3,
        "title": "The Course of Empire: Destruction",
        "artist": "Thomas Cole",
        "edition": "original",
        "medium": "Oil on canvas",
        "style": "Romanticism",
        "dimensions": "Unknown",
        "thumbnail": 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Cole_Thomas_The_Course_of_Empire_Destruction_1836.jpg/1280px-Cole_Thomas_The_Course_of_Empire_Destruction_1836.jpg',
        "year_of_creation": "1836",
        "provenance": "Private collection; American art museums",
        "listing_date": "24-6-2026"
    },
    {
        "id": 4,
        "title": "The Raft of the Medusa",
        "artist": "Théodore Géricault",
        "edition": "original",
        "medium": "Oil on canvas",
        "style": "Romanticism",
        "dimensions": "491 × 716 cm",
        "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/JEAN_LOUIS_TH%C3%89ODORE_G%C3%89RICAULT_-_La_Balsa_de_la_Medusa_%28Museo_del_Louvre%2C_1818-19%29.jpg/1280px-JEAN_LOUIS_TH%C3%89ODORE_G%C3%89RICAULT_-_La_Balsa_de_la_Medusa_%28Museo_del_Louvre%2C_1818-19%29.jpg",
        "year_of_creation": "1819",
        "provenance": "Louvre Museum",
        "listing_date": "24-6-2026"
    },
    {
        'id': 5,
        'title': 'Man in Armour',
        'artist': 'Rembrandt van Rijn',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Baroque',
        'dimensions': 'Unknown',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/a/ab/Rembrandt_Man_in_Armour.jpg?utm_source=commons.wikimedia.org&utm_campaign=index&utm_content=original',
        'year_of_creation': '1655',
        'provenance': 'Kelvingrove Art Gallery and Museum',
        'listing_date': '24-6-2026'
    },
    {
        'id': 6,
        'title': 'The Course of Empire: Desolation',
        'artist': 'Thomas Cole',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Romanticism',
        'dimensions': '100 × 161 cm',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Cole_Thomas_The_Course_of_Empire_Desolation_1836.jpg/1280px-Cole_Thomas_The_Course_of_Empire_Desolation_1836.jpg',
        'year_of_creation': '1836',
        'provenance': 'New-York Historical Society',
        'listing_date': '24-6-2026'
    },
    {
        'id': 7,
        'title': 'Guernica',
        'artist': 'Pablo Picasso',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Cubism',
        'dimensions': '349 × 776 cm',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/en/7/74/PicassoGuernica.jpg',
        'year_of_creation': '1937',
        'provenance': 'Museo Reina Sofía',
        'listing_date': '24-6-2026'
    },
    {
        'id': 8,
        'title': 'The Starry Night',
        'artist': 'Vincent van Gogh',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Post-Impressionism',
        'dimensions': '74 × 92 cm',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/1280px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg',
        'year_of_creation': '1889',
        'provenance': 'Museum of Modern Art',
        'listing_date': '24-6-2026'
    },
    {
        'id': 9,
        'title': 'The Persistence of Memory',
        'artist': 'Salvador Dalí',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Surrealism',
        'dimensions': '24 × 33 cm',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/en/d/dd/The_Persistence_of_Memory.jpg',
        'year_of_creation': '1931',
        'provenance': 'Museum of Modern Art',
        'listing_date': '24-6-2026'
    },
    {
        'id': 10,
        'title': 'Girl with a Pearl Earring',
        'artist': 'Johannes Vermeer',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Baroque',
        'dimensions': '44.5 × 39 cm',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/0/0f/1665_Girl_with_a_Pearl_Earring.jpg',
        'year_of_creation': '1665',
        'provenance': 'Mauritshuis',
        'listing_date': '24-6-2026'
    },
    {
        'id': 11,
        'title': 'The Night Watch',
        'artist': 'Rembrandt van Rijn',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Baroque',
        'dimensions': '363 × 437 cm',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/La_ronda_de_noche%2C_por_Rembrandt_van_Rijn.jpg/960px-La_ronda_de_noche%2C_por_Rembrandt_van_Rijn.jpg',
        'year_of_creation': '1642',
        'provenance': 'Rijksmuseum',
        'listing_date': '24-6-2026'
    },
    {
        'id': 12,
        'title': 'Vercingetorix Throwing Down His Weapons at the Feet of Julius Caesar',
        'artist': 'Lionel Royer',
        'edition': 'original',
        'medium': 'Oil on canvas',
        'style': 'Academic art',
        'dimensions': 'Unknown',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Lionel_Royer_-_Vercingetorix_Throwing_down_His_Weapons_at_the_feet_of_Julius_Caesar.jpg',
        'year_of_creation': '1899',
        'provenance': 'Musée Crozatier',
        'listing_date': '24-6-2026'
    },
    {
        'id': 13,
        'title': 'American Gothic',
        'artist': 'Grant Wood',
        'edition': 'original',
        'medium': 'Oil on beaverboard',
        'style': 'Regionalism',
        'dimensions': '78 × 65 cm',
        'thumbnail': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Grant_Wood_-_American_Gothic_-_Google_Art_Project.jpg/960px-Grant_Wood_-_American_Gothic_-_Google_Art_Project.jpg',
        'year_of_creation': '1930',
        'provenance': 'Art Institute of Chicago',
        'listing_date': '24-6-2026'
    }
]

for item in artworks:
    Artwork.objects.create(
        title=item["title"],
        artist=item["artist"],
        edition=item["edition"],
        medium=item["medium"],
        style=item["style"],
        dimensions=item["dimensions"],
        thumbnail=item["thumbnail"],
        year_of_creation=item["year_of_creation"],
        provenance=item["provenance"],
        listing_date=datetime.strptime(
            item["listing_date"],
            "%d-%m-%Y"
        ).date()
    )

def get_all_artworks(request):
    artworks = Artwork.objects.filter(active=True)
    return render(request, "artwork/all_artworks.html", {"artwork": artworks})

def get_artwork_by_id_2(request, artwork_id):
    artwork = get_object_or_404(artwork, id=artwork_id)
    return render(request, "artwork/artwork.html", {"artwork": artwork_info})


def index(request):
    return render(request, "artwork/all_artworks.html", {
        "artworks": artworks
    })


def get_artwork_by_id(request, id):
    artwork_info = [x for x in artworks if x['id'] == id][0]

    return render(request, "artwork/artwork.html", {
        "artwork": artwork_info
    })
