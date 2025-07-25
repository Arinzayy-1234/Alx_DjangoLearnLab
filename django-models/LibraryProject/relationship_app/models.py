from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.name} ; author_id = {self.pk}'

class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name = 'books')

    def __str__(self):
        return f'{self.title} by {self.author.name}'
    

class Library(models.Model):
    name = models.CharField(max_length = 50)
    books = models.ManyToManyField(Book, related_name = 'libraries')

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length = 50)
    library = models.ForeignKey(Library, on_delete = models.CASCADE, related_name = 'librarians')

    def __str__(self):
        return f'{self.name} -> {self.library.name} library'