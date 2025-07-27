from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    categories = [
    ("FICTION", "Fiction"),
    ("NON_FICTION", "Non-Fiction"),
    ("MYSTERY", "Mystery"),
    ("THRILLER", "Thriller"),
    ("ROMANCE", "Romance"),
    ("SCI_FI", "Science Fiction"),
    ("FANTASY", "Fantasy"),
    ("HISTORICAL", "Historical Fiction"),
    ("HORROR", "Horror"),
    ("BIOGRAPHY", "Biography"),
    ("MEMOIR", "Memoir"),
    ("SELF_HELP", "Self-Help"),
    ("POETRY", "Poetry"),
    ("DRAMA", "Drama"),
    ("ADVENTURE", "Adventure"),
    ("YA", "Young Adult"),
    ("CHILDRENS", "Children’s"),
    ("DYSTOPIAN", "Dystopian"),
    ("CRIME", "Crime"),
    ("GRAPHIC", "Graphic Novel"),
    ("CLASSIC", "Classic"),
    ("HUMOR", "Humor"),
    ("PARANORMAL", "Paranormal"),
    ("CONTEMPORARY", "Contemporary"),
    ("POLITICAL", "Political"),
]
    category = models.CharField(max_length=50, choices=categories, unique=True)

    def __str__(self):
        return self.get_category_display()

class Book(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])

    @classmethod
    def total_books(cls):
        return cls.objects.count()

    def __str__(self):
        return self.title
