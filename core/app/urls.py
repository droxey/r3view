from django.conf.urls import url
from core.app import views


urlpatterns = [
    url(r'^ajax-auth/(?P<backend>[^/]+)/$', views.ajax_auth, name='oauth-ajax-auth'),
    url(r'^dashboard/(?P<username>[\w.@+-]+)/$', views.dashboard, name='dashboard'),
    url(r'^code/(?P<slug>[\w.@+-]+)/$', views.session, name='session'),
    url(r'^launch/$', views.launch, name='launch'),
    url(r'^terms/$', views.terms, name='terms'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url(r'^$', views.home, name='home'),
]
