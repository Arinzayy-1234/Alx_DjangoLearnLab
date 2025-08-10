
from . models import Author, Book

from rest_framework import serializers
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publication_year']

    def validate_publication_year(self,data):
        current_year = date.today().year
        if data < current_year:
            raise serializers.ValidationError("Publication year can't be in the future.")
        return data




class AuthorSerializer(serializers.ModelSerializer):

    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name','books']