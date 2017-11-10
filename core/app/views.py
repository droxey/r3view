import json

from django.conf import settings
from django.contrib.auth import logout as auth_logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render, redirect

from social_core.backends.oauth import BaseOAuth1, BaseOAuth2
from social_django.models import UserSocialAuth
from social_django.utils import psa

from core.app.models import CodeSession, CodeSessionForm


@login_required
def dashboard(request, username):
    return render(request, 'dashboard.html', {})


@login_required
def session(request, slug):
    ws_url = '//{}:{}/{}'.format(settings.SITE_DOMAIN,
                                 settings.SOCKJS_PORT,
                                 settings.SOCKJS_WS_ECHO)
    try:
        session = CodeSession.objects.get(slug=slug)
        oauth = UserSocialAuth.objects.get(user=session.owner, provider='github')
        token = oauth.extra_data['access_token']
    except CodeSession.DoesNotExist:
        return redirect('launch')
    except UserSocialAuth.DoesNotExist:
        token = None

    return render(request, 'session.html', {
        'ws_url': ws_url,
        'token': token,
        'session': session
    })


@login_required
def launch(request):
    if request.method == "POST":
        form = CodeSessionForm(request.POST)
        if form.is_valid():
            form.owner = request.user
            form.driver = request.user
            form.save()
            return redirect('session', slug=session.slug)
    else:
        form = CodeSessionForm()
    return render(request, 'launch.html', {
        'form': form,
    })


def home(request):
    if request.user.is_authenticated():
        return redirect('dashboard', username=request.user.username)
    return render(request, 'home.html', {})


def terms(request):
    return render(request, 'terms.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})


def logout(request):
    auth_logout(request)
    return redirect('/')


@psa('social:complete')
def ajax_auth(request, backend):
    if isinstance(request.backend, BaseOAuth1):
        token = {
            'oauth_token': request.REQUEST.get('access_token'),
            'oauth_token_secret': request.REQUEST.get('access_token_secret'),
        }
    elif isinstance(request.backend, BaseOAuth2):
        token = request.REQUEST.get('access_token')
    else:
        raise HttpResponseBadRequest('Unkown backend type!')
    user = request.backend.do_auth(token, ajax=True)
    login(request, user)
    data = {'id': user.id, 'username': user.username, 'token': token}
    return HttpResponse(json.dumps(data), mimetype='application/json')
