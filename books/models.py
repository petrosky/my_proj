from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=75)


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})

