from django.db import models
from django.utils.text import slugify

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=15, primary_key=True)
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    genre = models.ManyToManyField(Genre)
    desc = desc = models.TextField(blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.name)
        super(Author, self).save()


class Library(models.Model):
    book = models.CharField(max_length=30, primary_key=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    qty = models.PositiveIntegerField()
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.book

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.slug = slugify(self.book)
        super(Library, self).save()