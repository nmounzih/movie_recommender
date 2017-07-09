from django.shortcuts import render
from rest_framework import viewsets
from .models import Rater, Movie, Rating
from .serializers import RaterSerializer, MovieSerializer, RatingSerializer


class RaterViewSet(viewsets.ModelViewSet):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


def index(request):
    movies = Movie.objects.all()
    return render(request, 'recommender_app/index.html', {'movies': movies})
