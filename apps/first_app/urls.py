from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'registration$', views.registration),
    url(r'login$', views.login),
    url(r'success$', views.success),
    url(r'mlb$', views.mlbindex),
    url(r'nfl$', views.nflindex),
    url(r'nba$', views.nbaindex),
    url(r'music$', views.music),
    url(r'about$', views.about),
]  