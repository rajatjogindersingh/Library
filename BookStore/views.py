from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import LibrarySerializer, AuthorSerializer, GenreSerializer
from .models import Library, Author, Genre
from rest_framework.response import Response
from BookStore import PostData,GetData

# Create your views here.
class GenreViews(APIView):

    def get(self, request, *args, **kwargs):
        search_param = dict()
        pages = dict()
        page_filter = ['page', 'per_page']
        for key,value in request.GET.items():
            if key in page_filter:
                pages[key] = value
            else:
                search_param[key] = value
        genre, status = GetData(search_param=search_param, kwargs=kwargs, db_model=Genre,
                                db_serializer=GenreSerializer, pages=pages)
        return Response(genre, status=status)

    def post(self, request):
        json_data = request.data
        if not json_data:
            return Response({"message":"No Data Found"}, 400)
        genre, status = PostData(json_data, GenreSerializer)
        return Response(genre, status)

    def put(self, request, *args, **kwargs):
        json_data = request.data
        if not (json_data and kwargs):
            return Response({"message":"Invalid Data/URL"}, 400)

        genre, status = GetData(kwargs=kwargs, db_model=Genre, db_serializer=GenreSerializer, serialized_output=False)
        if status != 200:
            return Response({"message": "Record not Found"}, 400)

        genre, status = PostData(json_data, GenreSerializer, put_obj=genre[0])
        return Response(genre, status)

    def delete(self, request, *args, **kwargs):
        if not kwargs:
            return Response({"message": "Invalid URL"}, 400)

        genre, status = GetData(kwargs=kwargs, db_model=Genre, db_serializer=GenreSerializer, serialized_output=False)
        if status != 200:
            return Response({"message": "Record not Found"}, 400)

        genre[0].delete()
        return Response({"message":"Record successfully deleted"}, status=status)


class AuthorViews(APIView):

    def get(self, request, *args, **kwargs):
        search_param = dict()
        pages = dict()
        page_filter = ['page', 'per_page']
        for key,value in request.GET.items():
            if key in page_filter:
                pages[key] = value
            else:
                search_param[key] = value
        genre, status = GetData(search_param=search_param, kwargs=kwargs, db_model=Author,
                                db_serializer=AuthorSerializer, pages=pages)
        return Response(genre, status=status)

    def post(self, request):
        json_data = request.data
        if not json_data:
            return Response({"message":"No Data Found"}, 400)
        genre, status = PostData(json_data, AuthorSerializer)
        return Response(genre, status)

    def put(self, request, *args, **kwargs):
        json_data = request.data
        if not (json_data and kwargs):
            return Response({"message":"Invalid Data/URL"}, 400)

        author, status = GetData(kwargs=kwargs, db_model=Author, db_serializer=AuthorSerializer, serialized_output=False)
        if status != 200:
            return Response({"message": "Record not Found"}, 400)

        author, status = PostData(json_data, AuthorSerializer, put_obj=author[0])
        return Response(author, status)

    def delete(self, request, *args, **kwargs):
        if not kwargs:
            return Response({"message": "Invalid URL"}, 400)

        author, status = GetData(kwargs=kwargs, db_model=Author, db_serializer=AuthorSerializer, serialized_output=False)
        if status != 200:
            return Response({"message": "Record not Found"}, 400)

        author[0].delete()
        return Response({"message":"Record successfully deleted"}, status=status)

class LibraryViews(APIView):

    def get(self, request, *args, **kwargs):
        search_param = dict()
        pages = dict()
        page_filter = ['page', 'per_page']
        for key,value in request.GET.items():
            if key in page_filter:
                pages[key] = value
            else:
                search_param[key] = value
        genre, status = GetData(search_param=search_param, kwargs=kwargs, db_model=Library,
                                db_serializer=LibrarySerializer, pages=pages)
        return Response(genre, status=status)

    def post(self, request):
        json_data = request.data
        if not json_data:
            return Response({"message":"No Data Found"}, 400)
        genre, status = PostData(json_data, LibrarySerializer)
        return Response(genre, status)

    def put(self, request, *args, **kwargs):
        json_data = request.data
        if not (json_data and kwargs):
            return Response({"message":"Invalid Data/URL"}, 400)

        library, status = GetData(kwargs=kwargs, db_model=Library, db_serializer=LibrarySerializer, serialized_output=False)
        if status != 200:
            return Response({"message": "Record not Found"}, 400)

        library, status = PostData(json_data, LibrarySerializer, put_obj=library[0])
        return Response(library, status)

    def delete(self, request, *args, **kwargs):
        if not kwargs:
            return Response({"message": "Invalid URL"}, 400)

        library, status = GetData(kwargs=kwargs, db_model=Library, db_serializer=LibrarySerializer, serialized_output=False)
        if status != 200:
            return Response({"message": "Record not Found"}, 400)

        library[0].delete()
        return Response({"message":"Record successfully deleted"}, status=status)
