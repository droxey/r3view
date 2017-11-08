from django.conf import settings
from django.shortcuts import render


def dashboard(request, username):
    return render(request, 'dashboard.html', {})


def session(request, username, session_id=None):
    ws_url = '//{}:{}/{}'.format(settings.SITE_DOMAIN,
                                 settings.SOCKJS_PORT,
                                 settings.SOCKJS_WS_ECHO)
    return render(request, 'session.html', {
        'ws_url': ws_url,
    })


def home(request):
    return render(request, 'home.html', {})


def terms(request):
    return render(request, 'terms.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})
