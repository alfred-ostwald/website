from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import *

def index(request):
    # get something from an object model here
    # eg the list of the top bar links
    titles = TopBar.objects.all()
    context = {'top_bar_headers' : titles}
    return render(request,'website/index.html',context)

def album_overview(request, album_id):
    """
    album_info:
    an array of small picture frames, click on to enlarge and browse album
    """
    return HttpResponse("this is album %s" % album_id)

def pictures(request, album_id):
    response = "these are the pics for album %s" % album_id
    return HttpResponse(response % album_id)

def picture_view(request, picture_id):
    # try:
    #     picture = Picture.objects.get(pk=picture_id)
    # except Picture.DoesNotExist:
    #     raise Http404("Picture not found")
    # return render(request,'website/picture_view.html',\
    #     {'picture': picture})
    picture = get_object_or_404(Picture,pk=picture_id)
    context = {'picture_id' : picture}
    return render(request,'website/picture_view.html',context)

    # this from SO to show an image - not sure if it's what i want though
    # try:
    #     with open(valid_image,"rb") as f:
    #         return HttpResponse(f.read(),content_type="image/jpeg")
    # except IOError:
    #     some other thing

# def galleries(request):
#
# def about(request):
#
# def contact(request):
#
# def login(request):
