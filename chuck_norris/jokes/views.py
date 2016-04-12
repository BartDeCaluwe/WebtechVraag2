from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic

from .models import Joke

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
joke_list = []

def fill_db():
	r.set('joke:1', "Dit is een goede mop")
	r.set('joke:2', "Dit is een betere mop")

# Create your views here.
def index(request):
	return render(request, 'quotes/index.html')

def joke(request):
	joke_list = r.keys('joke:*')
	jokes_text = []
	for j in joke_list:
		jokes_text.append(r.get(j))
	return render(request, 'jokes/joke.html', {'jokes': jokes_text})
