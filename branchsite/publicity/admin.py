from publicity.models import Event
from django.contrib import admin

class CommonMedia:
    js = (
        'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
        '/static/admin/dojo.js',
    )
    css = {
        'all': ('/static/admin/dojo.css',),
    }

admin.site.register(
    Event,
    list_display = ('title','start'),
    Media = CommonMedia,
)
