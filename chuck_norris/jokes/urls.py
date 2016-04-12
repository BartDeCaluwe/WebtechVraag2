from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<author_name>[A-z .-]+)/$', views.detail, name='detail'),
]
