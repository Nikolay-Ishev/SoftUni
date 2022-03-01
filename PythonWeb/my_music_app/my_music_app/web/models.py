from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
import re
from django.utils.deconstruct import deconstructible

# Create your models here.


VALIDATE_ONLY_L_N_U_EXCEPTION_MSG = "Ensure this value contains only letters, numbers, and underscore."


# IMG_MAX_SIZE_IN_MB = 5


# custom validator
def validate_only_letters_numbers_underscores(value):
    if not re.match(r'^[A-Za-z0-9_]+$', value):
        raise ValidationError(VALIDATE_ONLY_L_N_U_EXCEPTION_MSG)



class Profile(models.Model):
    USERNAME_MIN_LEN = 2
    USERNAME_MAX_LEN = 15
    MIN_AGE = 0

    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            MinLengthValidator(USERNAME_MIN_LEN),
            validate_only_letters_numbers_underscores,
        )
    )
    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators=(
            MinValueValidator(MIN_AGE),
        )
    )


class Album(models.Model):
    ALBUM_MAX_LEN = 30
    ARTIST_MAX_LEN = 30
    GENRE_MAX_LEN = 30
    MIN_PRICE = 0

    POP = "Pop Music"
    JAZZ = "Jazz Music"
    RB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIPHOP = "Hip Hop Music"
    OTHER = "Other"
    GENRES = [(x, x) for x in (POP, JAZZ, RB, ROCK, COUNTRY, DANCE, HIPHOP, OTHER)]

    name = models.CharField(
        max_length=ALBUM_MAX_LEN,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=GENRES,

    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    img_url = models.URLField()

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        )
    )
