from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Track, Album, Artist, Tag


admin.site.unregister(Group)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    search_fields = ["name"]


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    search_fields = ["title"]


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):

    readonly_fields = ["id", "uuid", "created_at", "updated_at"]
    list_display = ["title", "duration_seconds"]
    list_filter = ["instrument_type", "is_published"]
    autocomplete_fields = ["album", "tags"]

    fieldsets = (
        (
            None,
            {
                "fields": [
                    "id",
                    "uuid",
                ]
            },
        ),
        (
            "Details",
            {
                "fields": [
                    "title",
                    "album",
                    "duration_seconds",
                ]
            },
        ),
        (
            "Extra Info",
            {
                "fields": [
                    "lyrics",
                    "instrument_type",
                    "is_published",
                    "tags",
                ]
            },
        ),
        (
            "Dates",
            {
                "fields": [
                    "created_at",
                    "updated_at",
                ]
            },
        ),
    )
