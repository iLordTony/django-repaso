from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Editor(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()


class Author(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    authores = models.ManyToManyField(Author)
    editor = models.ForeignKey(Editor)
    publication_date = models.DateField()
    cover = models.ImageField(upload_to='covers')