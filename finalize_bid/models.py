from django.db import models
from django.artwork.models import Artwork
from django.user.models import Buyer


class Bid(models.Model):
    artwork = models.ForeignKey(
        Artwork,
        on_delete=models.CASCADE
    )

    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE
    )

    price = models.IntegerField()

    date_of_bid = models.DateTimeField(
        auto_now_add=True
    )

    expiration_date = models.DateTimeField()

    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.buyer} - {self.price}"
