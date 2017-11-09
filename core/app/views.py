from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request, username):
    return render(request, 'dashboard.html', {})


@login_required
def session(request, username, session_id=None):
    ws_url = '//{}:{}/{}'.format(settings.SITE_DOMAIN,
                                 settings.SOCKJS_PORT,
                                 settings.SOCKJS_WS_ECHO)
    return render(request, 'session.html', {
        'ws_url': ws_url,
        'is_debug': settings.DEBUG
    })


def home(request):
    return render(request, 'home.html', {})


def terms(request):
    return render(request, 'terms.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})
