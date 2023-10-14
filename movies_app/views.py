from django.shortcuts import render
from django.http import HttpResponse

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


def home(request):
    return HttpResponse('Welcome to the Movie Matcher API!')