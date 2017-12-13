import datetime

from django.db import models
from django.utils import timezone

class Album(models.Model):
    """
    each album will contain paths to pictures and other information
    could expand to allow for specific type of events, eg corporate or not
    """
    album_title = models.CharField(max_length=100)
    album_description = models.CharField(max_length=255,default='',blank=True)
    pub_date = models.DateTimeField('date published',auto_now_add=True)
    album_date = models.DateTimeField('event date',null=True,blank=True)
    album_location = models.CharField(max_length=100,default='',blank=True)

    def __str__(self):
        return self.album_title

    def __str__(self):
        return self.album_description

    def __str__(self):
        return self.album_location



class Picture(models.Model):
    """
    the paths to pictures uploaded to an album
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    picture_dir = models.CharField(max_length=100,default='dir')
    picture_file = models.CharField(max_length=100,default='file')
    picture_date = models.DateTimeField('picture date',null=True,blank=True)
    picture_description = models.CharField(max_length=255,default='',blank=True)

    def __str__(self):
        return self.picture_dir

    def __str__(self):
        return self.picture_file

    def __str__(self):
        return self.picture_description


class About(models.Model):
    """
    just a simple table with a text field for the About section
    provide a function to update the text
    """
    about_me = models.TextField()

    def __str__(self):
        return self.about_me

# class TopBar(model.Model):
#     """
#     object to hold all the links from the top bar:
#         Home
#         Galleries
#         About
#         Contact
#         Login
#     """
