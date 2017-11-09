import datetime
import json
import celery
import redis

from django.conf import settings
from django.contrib import auth
from django.utils import importlib


@celery.task
def get_user_by_session_key(session_key, extra_context=None):
    class MockRequest(object):
        pass

    engine = importlib.import_module(settings.SESSION_ENGINE)
    django_request = MockRequest()
    django_request.session = engine.SessionStore(session_key)
    user = auth.get_user(django_request)

    if extra_context:
        extra_context['user'] = user
        return extra_context
    return user
