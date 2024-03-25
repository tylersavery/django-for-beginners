from django.db import models
from django.core.validators import MaxLengthValidator, RegexValidator

from common.models import AbstractModel


class Tag(models.Model):

    NAME_MAX_LENGTH = 32
    NAME_RE = r"^[a-z0-9]+(?:[_.-][a-z0-9]+)*$"
    NAME_VALIDATORS = [
        MaxLengthValidator(NAME_MAX_LENGTH),
        RegexValidator(NAME_RE),
    ]

    name = models.CharField(
        max_length=10,
        unique=True,
        validators=NAME_VALIDATORS,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Artist(AbstractModel):

    name = models.CharField(max_length=125)
    avatar = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta(AbstractModel.Meta):
        verbose_name = "Artist"
        verbose_name_plural = "Artists"


class Album(AbstractModel):

    title = models.CharField(max_length=125)
    cover_art = models.URLField(blank=True, null=True)
    release_year = models.PositiveIntegerField()

    artist = models.ForeignKey(
        Artist,
        related_name="albums",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    class Meta(AbstractModel.Meta):
        verbose_name = "Album"
        verbose_name_plural = "Albums"


class Track(AbstractModel):

    class InstrumentType(models.TextChoices):
        INSTRUMENTAL = "instrumental", "Instrumental"
        ACAPELLA = "acapella", "Acapella"
        MIXED = "mixed", "Mixed"

    title = models.CharField(max_length=125)

    album = models.ForeignKey(
        Album,
        related_name="tracks",
        on_delete=models.CASCADE,
    )

    duration_seconds = models.IntegerField()
    lyrics = models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    instrument_type = models.CharField(
        max_length=16,
        choices=InstrumentType.choices,
        default=InstrumentType.MIXED,
    )

    tags = models.ManyToManyField(
        Tag,
        related_name="tracks",
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"
