from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from .models import Album, Song


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request,'music/index.html',context)

def detail(request,album_id):

    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("album does not exist")

    return render(request, 'music/detail.html',{'album':album})

def favorite(request,album_id):

    album=get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (KeyError,Song.DoesNotExist):
        return render(request, 'music/detail.html', {'album': album})
    else:
        selected_song.favorite_song=True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})





