from django.shortcuts import render_to_response
from django.http import HttpResponse
import simplejson

from models import Event

def home(request):
    events = Event.objects.order_by('start')[:3]
    return render_to_response('homepage.html', {'events':events})

def events_list(request):
    events = Event.objects.all()
    
    response = []
    for event in events:
        response.append({
            'title':event.title,
            'start':str(event.start)
        })

    return HttpResponse(simplejson.dumps(response), 'application/json')

def event_detail(request):
    event = Event.objects.get()
    return render_to_response('event_detail.html', {'event':event})
