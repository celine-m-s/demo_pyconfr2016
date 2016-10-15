from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView

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


class AddSpeakerView(CreateView):
    template_name = 'add_speaker.html'
    form_class = SpeakerForm
    success_url = reverse_lazy('index')


class UpdateSpeakerView(UpdateView):
    template_name = 'update_speaker.html'
    form_class = SpeakerForm
    success_url = reverse_lazy('index')
    queryset = Speaker.objects.all()
