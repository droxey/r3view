
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.core.urlresolvers import reverse
from django.db import models

from randomslugfield import RandomSlugField


class CodeSession(models.Model):
    slug = RandomSlugField(length=7, exclude_digits=True, exclude_vowels=True)
    name = models.CharField(max_length=120, null=True)
    description = models.TextField(null=True)
    repo_url = models.URLField('GitHub Repository URL', max_length=255,
        help_text='The URL to your PUBLIC GitHub repo. Starts with http(s).')
    repo_branch = models.CharField('Select Branch', max_length=80, default="master",
        help_text='Which branch would you like to review? Default: master.')
    repo_tree = JSONField(null=True)
    active_file = models.CharField(max_length=120, null=True)
    owner = models.ForeignKey(User, related_name="owner")
    driver = models.ForeignKey(User, related_name="driver")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('session', kwargs={'slug': self.slug})


class CodeSessionForm(forms.ModelForm):
    class Meta:
        model = CodeSession
        fields = ['repo_url', 'repo_branch']

    def __init__(self, *args, **kwargs):
        super(CodeSessionForm, self).__init__(*args, **kwargs)
        self.request = kwargs.pop('request', None);
        self.fields['repo_url'].required = True
        self.fields['repo_url'].widget.attrs = {
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': 'https://github.com/username/repository-name'
        }
        self.fields['repo_branch'].required = True
        self.fields['repo_branch'].widget.attrs = {
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': 'master'
        }
