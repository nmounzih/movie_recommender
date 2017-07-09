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
    movies = Movie.objects.all() #turn to top 20 later with averages
    return render(request, 'recommender_app/index.html', {'movies': movies})


def profile(request, id):
    r = Rater.objects.get(id=id)
    context = {}
    context['rater'] = r
    return render(request, 'recommender_app/profile.html', context)


def movie_detail(request, id):
    m = Movie.objects.get(id=id)
    context = {}
    context['movie'] = m
    return render(request, 'recommender_app/movie_detail.html', context)


def library(request):
    movies = Movie.objects.all()
    return render(request, 'recommender_app/library.html', {'movies': movies})
