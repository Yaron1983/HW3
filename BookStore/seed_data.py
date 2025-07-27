import os
import django
import random
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')  # החלף לשם הפרויקט שלך
django.setup()

from library.models import Author, Genre, Book

# ריקון טבלאות
Book.objects.all().delete()
Genre.objects.all().delete()
Author.objects.all().delete()

# יצירת ז'אנרים
genres = [
    "FICTION", "NON_FICTION", "MYSTERY", "THRILLER", "ROMANCE", "SCI_FI",
    "FANTASY", "HISTORICAL", "HORROR", "BIOGRAPHY", "MEMOIR", "SELF_HELP",
    "POETRY", "DRAMA", "ADVENTURE", "YA", "CHILDRENS", "DYSTOPIAN", "CRIME",
    "GRAPHIC", "CLASSIC", "HUMOR", "PARANORMAL", "CONTEMPORARY", "POLITICAL"
]
genre_objs = [Genre.objects.create(category=g) for g in genres]

# יצירת סופרים
authors_data = [
    {"first_name": "George", "last_name": "Orwell", "birth_date": "1903-06-25"},
    {"first_name": "Jane", "last_name": "Austen", "birth_date": "1775-12-16"},
    {"first_name": "J.K.", "last_name": "Rowling", "birth_date": "1965-07-31"},
    {"first_name": "Isaac", "last_name": "Asimov", "birth_date": "1920-01-02"},
    {"first_name": "Stephen", "last_name": "King", "birth_date": "1947-09-21"},
]
author_objs = [Author.objects.create(**data) for data in authors_data]

# יצירת ספרים
titles = [
    "1984",
    "Pride and Prejudice",
    "Harry Potter and the Sorcerer's Stone",
    "Foundation",
    "The Shining"
]

for i in range(len(titles)):
    Book.objects.create(
        title=titles[i],
        author=author_objs[i],
        genre=random.choice(genre_objs),
        publication_date=timezone.now(),
        rating=random.randint(1, 5),
    )

print("✅ Database seeded successfully.")
