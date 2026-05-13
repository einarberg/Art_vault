from django.db import models
from artwork.models import Artwork
from user.models import Buyer


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


class Contact_information(models.Model):
    national_id = CharField(max_length=100)

    buyer = models.ForeignKey(
        Buyer,
        on_delete=models.CASCADE,
        related_name='finalize_bid'
    )

    bid = models.ForeignKey(
        Bid,
        on_delete=models.CASCADE,
        related_name='finalize_bid'
    )

    Street_name = CharField(max_length=100)
    City = CharField(max_length=100)
    Postal_code = CharField(max_length=100)
    Country = CharField(max_length=100)

