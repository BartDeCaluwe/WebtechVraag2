from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic

from .models import Joke

import redis
import random
import json

r = redis.StrictRedis(host='localhost', port=6379, db=0)
joke_list = []
file = "C:/Users/Bart/Desktop/Webtech/WebtechVraag2/Jokes.json";

# Create your views here.
def index(request):
	return render(request, 'jokes/index.html')

def joke(request, voornaam, achternaam):
	jokes = json.loads(file)
	jokes_text = jokes[random.randint(1, jokes.length)]
	r.set(jokes_text)
	for j in joke_list:
		jokes_text.append(r.get(j))
	return render(request, 'jokes/joke.html', {'jokes': jokes_text, 'voornaam': voornaam, 'achternaam': achternaam})
