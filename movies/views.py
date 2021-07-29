from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Movie

# Create your views here.
@login_required
def home(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/home.html', context)
