from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie
# Create your views here.
def home(request):
    return render(request, 'home.html')

def movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        try : 
            if form.is_valid():
                form.save()
                return redirect('/show')
        except: 
            pass
    else:
        form = MovieForm()
    return render(request, 'index.html', {'form': form})

def show(request):
    movies = Movie.objects.all()
    return render(request,'show.html', {'movies': movies})

def edit(request, mid):
    movie = Movie.objects.get(mid=mid)
    return render(request, 'edit.html', {'movie': movie})

def update(request, mid):
    movie = Movie.objects.get(mid=mid)
    form = MovieForm(request.POST, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'movie': movie})

def delete(request, mid):
    movie = Movie.objects.get(mid=mid)
    movie.delete()
    return redirect('/show')