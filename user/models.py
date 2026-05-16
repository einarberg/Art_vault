from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthUser(AbstractUser):
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class User(models.Model):
    auth_user = models.OneToOneField(
        AuthUser,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    bio = models.TextField(blank=True, null=True)
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
