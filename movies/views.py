# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from movies.models import Category, Movie
from movies.serializers import CategorySerializer, MovieSerializer


# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
