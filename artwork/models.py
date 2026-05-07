from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    bio = models.TextField(blank=True)
    cover_image = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Buyer(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.name
# Maybe payment information?


class Seller(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.name


class Artist(models.Model):
    seller = models.OneToOneField(
        Seller,
        on_delete=models.CASCADE
    )


class Gallery(models.Model):
    seller = models.OneToOneField(
        Seller,
        on_delete=models.CASCADE
    )

    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)


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
