from django.conf.urls import url

from .views import index, add_speaker, AddSpeakerView, UpdateSpeakerView

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^add_speaker/$', add_speaker, name="add_speaker"),
    url(
        r'^add_speaker_cbv/$', AddSpeakerView.as_view(), name="add_speaker_cbv"
    ),
    url(
        r'^update_speaker/(?P<pk>\d+)$',
        UpdateSpeakerView.as_view(),
        name="update_speaker"
    ),
]
