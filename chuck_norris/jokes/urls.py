from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<voornaam>[A-z .-]+)&(?P<achternaam>[A-z .-])/$', views.joke, name='joke'),
]
