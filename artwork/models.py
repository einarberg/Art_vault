from django.db import models
from user.models import Seller
from user.models import Artist


class Style(models.Model):
    style = models.CharField(max_length=100)
    explanation = models.CharField(max_length=200)


class Artwork(models.Model):
    seller = models.ForeignKey(
        Seller,
        on_delete=models.CASCADE,
        related_name='artworks'
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='artworks'
    )
    
    title = models.CharField(max_length=200)

    dimensions = models.CharField(max_length=100)
    edition = models.CharField(max_length=100, blank=True)

    thumbnail = models.ImageField(
        upload_to='artwork_thumbnails/',
        blank=True,
        null=True
    )

    medium = models.CharField(max_length=100)
    style = models.ForeignKey(
        Style,
        on_delete=models.CASCADE,
        related_name='artworks'
    )
    bid_price = models.IntegerField()

    listing_date = models.DateField()

    year_of_creation = models.IntegerField()

    provenance = models.TextField(blank=True)

    bid_status = models.CharField(max_length=50)

    start_bid_price = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Picture(models.Model):
    artwork = models.ForeignKey(
        Artwork,
        on_delete=models.CASCADE,
        related_name='pictures'
    )

    image = models.ImageField(
        upload_to='artwork_gallery/'
    )
