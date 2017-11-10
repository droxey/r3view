
from django import forms
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
    repo_tree = JSONField(null=True)
    active_file = models.CharField(max_length=120, blank=True, null=True)
    owner = models.ForeignKey(User, related_name="owner")
    driver = models.ForeignKey(User, related_name="driver")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CodeSessionForm(forms.ModelForm):
    name = forms.CharField(
        help_text="Assign a friendly name to this code review session. Limit: 120 characters.",
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(
        label='Topic / Description',
        help_text="Let your collaborators know what you're working on.",
        widget=forms.Textarea(attrs={'class': 'form-control'}))
    repo_url = forms.CharField(
        label='GitHub Repository URL',
        help_text='The URL to your PUBLIC GitHub repo. Starts with http(s).',
        widget=forms.TextInput(attrs={'class': 'form-control', 'rows': 10}))
    repo_branch = forms.CharField(
        label='Review Branch',
        help_text='Which branch would you like to review? Default: master.',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    repo_tree = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CodeSession
        fields = ['name', 'description', 'repo_url', 'repo_branch', 'repo_tree']

