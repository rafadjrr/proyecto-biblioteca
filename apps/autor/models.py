from django.db import models

# Create your models here.

class Autor(models.Model):
    """Model definition for Autor."""

    # TODO: Define fields here
    first_name = models.CharField('name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    nationalice = models.CharField('nationalize', max_length=30)
    age = models.PositiveIntegerField()

    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autors'

    def __str__(self):
        """Unicode representation of Autor."""
        return self.first_name + ' ' + self.last_name
