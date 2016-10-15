from django.shortcuts import render, redirect

from .models import Speaker
from .forms import SpeakerForm


def index(request):
    speakers = Speaker.objects.all()
    return render(request, 'index.html', {'speakers': speakers})


def add_speaker(request):
    if request.method == 'POST':
        form = SpeakerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SpeakerForm()
    return render(request, 'add_speaker.html', {'form': form})
