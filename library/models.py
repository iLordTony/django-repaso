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

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Editors"

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=30)
    # o verbose_name='value' doesn't work ManyToManyField o ForeignKey
    surname = models.CharField('last name', max_length=30)
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)

    def __unicode__(self):
        return '%s %s' % (self.name, self.surname)


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    editor = models.ForeignKey(Editor)
    publication_date = models.DateField(blank=True, null=True)
    cover = models.ImageField(upload_to='covers')

    def __unicode__(self):
        return self.title
