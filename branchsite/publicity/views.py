from django.shortcuts import render_to_response
from django.http import HttpResponse
import simplejson

from models import Event

def home(request):
    event = Event.objects.get()
    return render_to_response('homepage.html', {'event':event})

def events_list(request):
    events = Event.objects.all()
    
    response = []
    for event in events:
        response.append({
            'title':event.title,
            'start':str(event.start)
        })

    return HttpResponse(simplejson.dumps(response), 'application/json')
