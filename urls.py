from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<album_id>[0-9]+)/$', views.album_overview,name='album overview'),
    url(r'^(?P<album_id>[0-9]+)/pictures/$', views.pictures,name='pictures')
]
