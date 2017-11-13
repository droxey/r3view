import json

from django.conf import settings
from django.contrib.auth import logout as auth_logout, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic import DetailView

from social_core.backends.oauth import BaseOAuth1, BaseOAuth2
from social_django.models import UserSocialAuth
from social_django.utils import psa

from core.app.models import CodeSession, CodeSessionForm


@login_required
def dashboard(request, username):
    sessions = CodeSession.objects.filter(owner=request.user)
    return render(request, 'app/dashboard.html', {
        'sessions': sessions
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

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.owner = self.request.user
        obj.driver = self.request.user
        obj.save()
        return JsonResponse({'url': obj.get_absolute_url()})


class CodeSessionDetailView(AjaxableResponseMixin, DetailView):
    """ GET. Gets data about a user. """
    model = CodeSession
    template_name = 'app/session.html'

    def get_queryset(self):
        """ Override `get_queryset`. This filtered query is then used
        in subsequent `get_object` calls to fetch specific objects. """
        queryset = super(CodeSessionDetailView, self).get_queryset()
        return queryset.filter(owner=self.request.user)

    def get_object(self, queryset=None):
        return super(CodeSessionDetailView, self).get_object(queryset=queryset)

    def get_context_data(self, **kwargs):
        context = super(CodeSessionDetailView,
                        self).get_context_data(**kwargs)
        session = context.get('codesession', None)
        oauth = UserSocialAuth.objects.get(user=session.owner, provider='github')
        ws_url = '/echo/'
        context.update({
            'token': oauth.extra_data['access_token'],
            'ws_url': settings.WS_URL,
            'session': session
        })
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
