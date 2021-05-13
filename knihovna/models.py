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


class Book(models.Model):
    name = models.CharField(max_length=150, verbose_name="Název knihy", help_text='Zadejte název knihy.')
    genres = models.ManyToManyField(Genre, help_text="Vyberte žánr knihy.")
    date = models.DateField(verbose_name="Datum vydání", help_text="Zadejte datum vydání knihy.")
    pages = models.IntegerField(blank=True, null=True, verbose_name="Počet stran", help_text="Zadejte počet stran.")
    rate = models.FloatField(default=5.0, validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], null=True,
                             help_text="Zadejte hodnocení od 1.0 - 10.0", verbose_name="Hodnocení")
    isbn = models.CharField(max_length=17, verbose_name="ISBN", help_text="Zadejte ISBN kód knihy.")

    class Meta:
        ordering = ["date", "name"]

    def __str__(self):
        return f"{self.name}, year: {str(self.date.year)}, rate: {str(self.rate)}"

    def get_absolute_url(self):
        return reverse('kniha-detail', args=[str(self.id)])
