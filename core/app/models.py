
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

from randomslugfield import RandomSlugField


class CodeSession(models.Model):
    slug = RandomSlugField(length=settings.RANDOMSLUG_LENGTH, exclude_digits=True, exclude_vowels=True, editable=False)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    repo_url = models.URLField(max_length=255)
    repo_branch = models.CharField(max_length=80, default="master")
    repo_tree = JSONField()
    active_file = models.CharField(max_length=120, blank=True, null=True)
    owner = models.ForeignKey(User, related_name="owner")
    driver = models.ForeignKey(User, related_name="driver")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
