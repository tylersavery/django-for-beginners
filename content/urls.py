from django.urls import path

from . import views

urlpatterns = [
    path("tracks/", views.track_list, name="track_list"),
    path("tracks/edit/", views.track_edit, name="track_edit"),
    path("tracks/edit/<uuid:track_uuid>/", views.track_edit, name="track_edit"),
    path("tracks/delete/<uuid:track_uuid>/", views.track_delete, name="track_delete"),
    path("tracks/<uuid:track_uuid>/", views.track_detail, name="track_detail"),
]
