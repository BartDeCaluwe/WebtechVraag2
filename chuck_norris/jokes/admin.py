from django.contrib import admin

# Register your models here.

from .models import Joke

admin.site.unregister(Joke)
admin.site.register(Joke)
