import json

from django.conf import settings
from django.contrib.auth import logout as auth_logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from social_core.backends.oauth import BaseOAuth1, BaseOAuth2
from social_django.models import UserSocialAuth
from social_django.utils import psa

from core.app.models import CodeSession, CodeSessionForm


@login_required
def dashboard(request, username):
    return render(request, 'app/dashboard.html', {})


@login_required
def session(request, slug):
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


def home(request):
    if request.user.is_authenticated():
        return redirect('dashboard', username=request.user.username)
    return render(request, 'app/home.html', {})


def terms(request):
    return render(request, 'app/terms.html', {})


def privacy(request):
    return render(request, 'app/privacy.html', {})


def logout(request):
    auth_logout(request)
    return redirect('/')


class AjaxableResponseMixin(object):
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(data)
        else:
            return response


class CodeSessionCreate(LoginRequiredMixin, AjaxableResponseMixin, CreateView):
    """ POST. Creates a new CodeSession. """
    model = CodeSession
    form_class = CodeSessionForm


class CodeSessionDetailView(AjaxableResponseMixin, DetailView):
    """ GET. Gets data about a user. """
    model = CodeSession
    template = 'app/session.html'

    def get_queryset(self):
        """ Override `get_queryset`. This filtered query is then used
        in subsequent `get_object` calls to fetch specific objects. """
        queryset = super(CodeSession, self).get_queryset()
        return queryset.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        return super(CodeSession, self).get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        context = super(CodeSessionDetailView,
                        self).get_context_data(**kwargs)
        try:
            session = CodeSession.objects.get(slug=self.request.slug)
            oauth = UserSocialAuth.objects.get(user=session.owner, provider='github')
            context['token'] = oauth.extra_data['access_token']
        except CodeSession.DoesNotExist:
            return redirect('launch')
        except UserSocialAuth.DoesNotExist:
            context['token'] = None
        context['ws_url'] = settings.WS_URL
        context['session'] = session
        return context


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
