from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic

from .models import Movie, Actor

import redis

r = redis.StrictRedis(host='localhost', port=1234, db=0)
author_list = []

def fill_db():
    r.set('movie:1', "Lord of the Rings: The Fellowship of the Ring")
    r.set('movie:2', "Saving Private Ryan")
    r.set('movie:3', "Pulp Fiction")
    r.set('actor:1', "actors: Elijah Wood, Ian McKellen, Viggo Mortensen, Sean Astin")
    r.set('actor:2', "actors: Samuel L. Jackson, John Travolta, Uma Thurman, Bruce Willis")
    r.set('actor:3', "actors: Tom Hanks, Tom Sizemore, Edward Burns")
 

fill_db()

# Create your views here.
def index(request):
   
    movie_list = r.keys('author:*')
    movie_names = []
    for m in movie_list:
        movie_names.append(r.get(m))
    return render(request, 'movies/index.html', {'movies': movie_names})

def detail(request, movie_name):
    movie_list = r.keys('movie:*')
    actors = []
    for m in movie_list:
        if r.get(m) == movie_name:
            movie_id = m.split(':')[1]
            actors_id = r.keys('actors:' + movie_id + ':*')
    for a in actors_id:
        actors.append(r.get(a))
    #get_object_or_404(Quote, pk=quote_id)
    #try:
    #    quote = Quote.objects.get(pk=quote_id)
    #except Quote.DoesNotExist:
    #    raise Http404('Quote does not exist')
    return render(request, 'movie/detail.html', {'movie': movie_name, 'actors': actors})

