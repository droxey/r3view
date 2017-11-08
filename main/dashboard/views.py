from django.shortcuts import render


def dashboard(request, username):
    return render(request, 'dashboard.html', {})


def session(request, username, session_id=None):
    return render(request, 'session.html', {})


def home(request):
    return render(request, 'home.html', {})


def terms(request):
    return render(request, 'terms.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})
