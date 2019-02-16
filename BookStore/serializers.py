from rest_framework.serializers import ModelSerializer
from .models import Library, Author, Genre


class LibrarySerializer(ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'