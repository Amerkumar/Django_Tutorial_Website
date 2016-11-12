from django.http import Http404
from django.http import HttpResponse
from .models import Album
from django.template import loader
from django.shortcuts import render ,get_object_or_404

def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums' : all_albums}
    return render(request , 'music/index.html' ,context)


# def index(request):
#     all_albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#         'all_albums' : all_albums,
#     }
#     return HttpResponse(template.render( context , request ))

# def index(request):
#     all_albums = Album.objects.all()
#     html = ''
#     for album in all_albums:
#         url = '/music/' + str(album.id) + '/'
#         html += '<a href="' + url + '">'+album.album_title + url + '</a><br>'
#     return HttpResponse(html)

# def detail(request , album_id):
#     try :
#         album = Album.objects.get(pk=album_id)
#     except Album.DoesNotExist:
#         raise Http404("Album Does not Exist")

#     return render(request,'music/details.html', {'album' : album} )
def detail(request , album_id):
    album = get_object_or_404(Album,pk = album_id)
    return render(request,'music/details.html', {'album' : album} )