from django.contrib import admin


# Register your models here.
from .models import Track


class TrackAdmin(admin.ModelAdmin):
    fields = ('title', 'posted_by', )


admin.site.register(Track, TrackAdmin)
