from email.policy import default
from django.db import models
from apps.libro.models import *
# Create your models here.


class Reader(models.Model):
    """Model definition for Lector."""

    # TODO: Define fields here

    first_name = models.CharField('name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    nationalice = models.CharField('nationalize', max_length=30)
    age = models.PositiveIntegerField(default=0)

    class Meta:
        """Meta definition for Lector."""

        verbose_name = 'Lector'
        verbose_name_plural = 'Lectors'

    def __str__(self):
        """Unicode representation of Lector."""
        return self.first_name + ' ' + self.last_name

class Loan(models.Model):
    """Model definition for Prestamo."""

    # TODO: Define fields here
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    date_loan = models.DateTimeField(auto_now=False, auto_now_add=False)
    date_return = models.DateTimeField(
        auto_now=False,
        auto_now_add=False,
        blank=True,
        null=True
    )
    returned = models.BooleanField()
    class Meta:
        """Meta definition for Prestamo."""

        verbose_name = 'Loan'
        verbose_name_plural = 'Loans'

    def __str__(self):
        """Unicode representation of Prestamo."""
        return self.book + ' ' + self.reader
