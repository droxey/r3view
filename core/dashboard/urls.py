from django.conf.urls import *
from core.dashboard import views


urlpatterns = [
    url(r'^(?P<username>.*)/dashboard/$',
        views.dashboard,
        name='dashboard'),

    url(r'^(?P<username>.*)/session/(?P<session_id>.*)/$',
        views.session,
        name='session'),

    url(r'^terms/$', views.terms, name='terms'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^$', views.home, name='home'),
]
