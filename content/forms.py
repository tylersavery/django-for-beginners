from django import forms
from content.models import Album, Track


class TrackForm(forms.ModelForm):

    class Meta:
        model = Track

        fields = [
            "title",
            "album",
            "duration_seconds",
            "lyrics",
            "is_published",
        ]
