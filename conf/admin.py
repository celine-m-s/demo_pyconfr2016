from django.contrib import admin

# import from current repository
from .models import Speaker, Talk


class TalkTabularInline(admin.TabularInline):
    model = Talk
    extra = 1


class SpeakerAdmin(admin.ModelAdmin):
    model = Speaker
    inlines = (TalkTabularInline,)


admin.site.register(Speaker, SpeakerAdmin)
