from django.db import models
from django.user.models import Seller


class Artwork(models.Model):
    seller = models.ForeignKey(
        Seller,
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
    style = models.CharField(max_length=100)

    bid_price = models.IntegerField()

    listing_date = models.DateField()

    year_of_creation = models.IntegerField()

    provenance = models.TextField(blank=True)

    bid_status = models.CharField(max_length=50)

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
