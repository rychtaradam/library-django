from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse


def img_path(instance, filename):
    return "images/" + filename


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Název žánru",
                            help_text='Zadejte knižní žánr (např. román, komedie)')

    class Meta:
        ordering = ["name"]
        permissions = (("can_add_genres", "Create a new genre"), ("can_delete_genres", "Delete a genre"),
                       ("can_update_genres", "Update a genre"),)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Jmeno autora", help_text="Zadejte jméno autora.")

    class Meta:
        ordering = ["name"]
        permissions = (("can_add_authors", "Create a new authors"), ("can_delete_authors", "Delete a authors"),
                       ("can_update_authors", "Update a authors"),)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=150, verbose_name="Název knihy", help_text='Zadejte název knihy.')
    genre = models.ManyToManyField(Genre, help_text="Vyberte žánr knihy.")
    author = models.ManyToManyField(Author, help_text="Vyberte autora knihy.")
    date = models.DateField(default="1.1.2021", verbose_name="Datum vydání", help_text="Zadejte datum vydání knihy.")
    pages = models.IntegerField(blank=True, null=True, verbose_name="Počet stran", help_text="Zadejte počet stran.")
    rate = models.FloatField(default=5.0, validators=[MinValueValidator(1.0), MaxValueValidator(10.0)], null=True,
                             help_text="Zadejte hodnocení od 1.0 - 10.0", verbose_name="Hodnocení")
    isbn = models.CharField(max_length=17, verbose_name="ISBN", help_text="Zadejte ISBN kód knihy.")
    image = models.ImageField(help_text="Nahrejte obrázek přebalu knihy", upload_to=img_path, blank=True, null=True,
                              verbose_name="Fotka")

    class Meta:
        ordering = ["date", "name"]
        permissions = (("can_add_books", "Create a new books"), ("can_delete_books", "Delete a books"),
                       ("can_update_books", "Update a books"),)

    def __str__(self):
        return f"{self.name}, Rok vydání: {str(self.date.year)}, Hodnocení: {str(self.rate)}"

    def get_absolute_url(self):
        return reverse('kniha-detail', args=[str(self.id)])
