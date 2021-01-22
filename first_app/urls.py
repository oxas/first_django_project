from django.urls import path, re_path
from .views import homeHtml, home

urlpatterns = [
    re_path(r'^$', homeHtml, name='homeHtml'),
    path('/home', home, name = 'home')
]
