from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Název žánru",
                            help_text='Zadejte knižní žánr (např. román, komedie)')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
