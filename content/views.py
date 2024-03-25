from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from content.models import Track

from .forms import TrackForm


def track_list(request):

    tracks = Track.objects.all()
    template = loader.get_template("content/track_list.html")
    context = {"tracks": tracks}
    return HttpResponse(template.render(context, request))


def track_detail(request, track_uuid):

    track = get_object_or_404(Track, uuid=track_uuid)

    template = loader.get_template("content/track_detail.html")
    context = {"track": track}
    return HttpResponse(template.render(context, request))


def track_edit(request, track_uuid=None):

    track = get_object_or_404(Track, uuid=track_uuid) if track_uuid else None

    if request.method == "POST":

        form = TrackForm(request.POST, instance=track)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/content/tracks/")

    else:

        form = TrackForm(instance=track)

    template = loader.get_template("content/track_edit.html")
    context = {"form": form, "track": track}
    return HttpResponse(template.render(context, request))


def track_delete(request, track_uuid):

    if request.method == "POST":
        track = get_object_or_404(Track, uuid=track_uuid)
        track.delete()
        return HttpResponseRedirect("/content/tracks/")

    return HttpResponse("Method GET not allowed")
