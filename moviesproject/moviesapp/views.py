from django.http import HttpResponse

from .forms import MovieForm
from . models import Movie
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        "movie_list":movie
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movie':movie})

def add(request):
    if request.method=='POST':
        movie_name=request.POST.get('moviename',)
        movie_desc=request.POST.get('desc',)
        movie_year=request.POST.get('year',)
        image=request.FILES.get('image')

        movie=Movie(name=movie_name,desc=movie_desc,year=movie_year,image=image)
        movie.save()
    return render(request,"add.html")

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,"edit.html",{'form':form,'movie':movie})

def delete(request,id):
    if request.method=='POST':
       movie=Movie.objects.get(id=id)
       movie.delete()
       return redirect('/')
    return render(request,"delete.html")