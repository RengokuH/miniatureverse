from unicodedata import name
from django import forms
from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
# Create your models here.

class LandingPage(models.Model):
    name = models.CharField(max_length=255)
    animationText = models.CharField(max_length=255)
    # animationText2 = models.CharField(max_length=255, blank=True)
    insta_url = models.CharField(max_length=1000, default="", blank=True)
    twitter_url = models.CharField(max_length=1000, default="", blank=True)
    linktree_url = models.CharField(max_length=1000, default="", blank=True)
    discord_url = models.CharField(max_length=1000, default="", blank=True)
    opensea_url = models.CharField(max_length=1000, default="", blank=True)

    def __str__(self):
        return self.name

        

class Collection(models.Model):
    title = models.CharField(max_length=255)
    desc = RichTextField()
    photo = models.ImageField(upload_to = 'media/about/', blank=True)

    def __str__(self) -> str:
        return self.title

class CollectionsInfo(models.Model):
    title = models.CharField(max_length=255)
    desc = RichTextField(blank=True)
    opensea_url = models.CharField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to = 'media/about/')

    def __str__(self) -> str:
        return self.title

class Journey(models.Model):
    title = models.CharField(max_length=255)
    desc = RichTextField(blank=True)
    photo1 = models.ImageField(upload_to = 'media/about/', blank=True)
    photo2 = models.ImageField(upload_to = 'media/about/', blank=True)
    photo3 = models.ImageField(upload_to = 'media/about/', blank=True)
    photo4 = models.ImageField(upload_to = 'media/about/', blank=True)

    def __str__(self) -> str:
        return self.title

class Roadmap(models.Model):
    title = models.CharField(max_length=255)
    subtitle1 = models.CharField(max_length=255)
    date1 = models.CharField(max_length=255, blank= True)
    desc1 = RichTextField()
    subtitle2 = models.CharField(max_length=255, blank= True)
    date2 = models.CharField(max_length=255, blank= True)
    desc2 = RichTextField(blank=True)
    subtitle3 = models.CharField(max_length=255, blank= True)
    date3 = models.CharField(max_length=255, blank= True)
    desc3 = RichTextField(blank=True)
    subtitle4 = models.CharField(max_length=255, blank= True)
    date4 = models.CharField(max_length=255, blank= True)
    desc4 = RichTextField(blank=True)
    subtitle5 = models.CharField(max_length=255, blank= True)
    date5 = models.CharField(max_length=255, blank= True)
    desc5 = RichTextField(blank=True)

    def __str__(self) -> str:
        return self.title
    

class OurCollection(models.Model):

    # ptype = (
    #     ('web', 'web'),
    #     ('app', 'app'),
    #     ('active', 'active'),
    # )

    # stype = (
    #     ('Web', 'Web'),
    #     ('App', 'App'),
    # )

    title = models.CharField(max_length=255)
    desc = RichTextField(blank=True)
    # type = models.CharField(max_length=255,choices= type)
    date = models.CharField(max_length=150, default= '', blank= True)
    photo1 = models.ImageField(upload_to = 'media/projects/')
    photo2 = models.ImageField(blank = True, upload_to = 'media/projects/')
    photo3 = models.ImageField(blank = True, upload_to = 'media/projects/')
    photo4 = models.ImageField(blank = True, upload_to = 'media/projects/')
    photo5 = models.ImageField(blank = True, upload_to = 'media/projects/')
    # img_link = models.CharField(max_length=255, default= '', blank=True)
    opensea_link = models.CharField(max_length=1500, default= '', blank=True)

    def __str__(self) -> str:
        return self.title

class ComingSoon(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank= True)
    photo = models.ImageField(blank = True, upload_to = 'media/services/')

    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    email=models.CharField(max_length=500)
    date_of_contact = models.DateTimeField(auto_now=True)
    message=models.TextField(max_length=1500)

    def __str__(self) -> str:
        return self.email

class MyContact(models.Model):
    email=models.EmailField(max_length=1000, blank= True)

    def __str__(self) -> str:
        return self.email

