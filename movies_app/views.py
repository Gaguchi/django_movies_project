from django.shortcuts import render

# movies_app/views.py
from rest_framework import viewsets
from .models import Movie, Like, Match
from .serializers import MovieSerializer, LikeSerializer, MatchSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
