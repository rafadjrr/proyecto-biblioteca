from django.db import models
from apps.autor.models import *


class Category(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField('category', max_length=50)
    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

class Book(models.Model):
    """Model definition for Libro."""
    # TODO: Define fields here
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    autors = models.ManyToManyField(Autor)
    title = models.CharField('title', max_length=120)
    date = models.DateField('date from launch', auto_now=False, auto_now_add=False)
    front_page = models.ImageField(upload_to='front_page', height_field=None, width_field=None, max_length=None)
    view = models.PositiveIntegerField()
    

    class Meta:
        """Meta definition for Libro."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of books."""
        return self.title + ' ' + self.date
