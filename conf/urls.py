from django.conf.urls import url

from .views import index, add_speaker

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^add_speaker/$', add_speaker, name="add_speaker")
]
