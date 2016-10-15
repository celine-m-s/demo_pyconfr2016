from django.shortcuts import render

from .models import Speaker


def index(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})
