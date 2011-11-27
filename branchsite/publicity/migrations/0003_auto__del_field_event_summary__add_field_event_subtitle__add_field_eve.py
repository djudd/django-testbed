# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Event.summary'
        db.delete_column('publicity_event', 'summary')

        # Adding field 'Event.subtitle'
        db.add_column('publicity_event', 'subtitle', self.gf('django.db.models.fields.CharField')(default='Why the Police Are Not Part of the 99%', max_length=100), keep_default=False)

        # Adding field 'Event.location_directions'
        db.add_column('publicity_event', 'location_directions', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Event.summary'
        db.add_column('publicity_event', 'summary', self.gf('django.db.models.fields.CharField')(default='Why the Police Are Not Part of the 99%', max_length=100), keep_default=False)

        # Deleting field 'Event.subtitle'
        db.delete_column('publicity_event', 'subtitle')

        # Deleting field 'Event.location_directions'
        db.delete_column('publicity_event', 'location_directions')


    models = {
        'publicity.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration_hours': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'location_directions': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['publicity']
