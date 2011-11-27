# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Event.location_directions'
        db.alter_column('publicity_event', 'location_directions', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Event.location_address'
        db.alter_column('publicity_event', 'location_address', self.gf('django.db.models.fields.CharField')(max_length=100, null=True))

        # Changing field 'Event.duration_hours'
        db.alter_column('publicity_event', 'duration_hours', self.gf('django.db.models.fields.FloatField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Event.location_directions'
        db.alter_column('publicity_event', 'location_directions', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Event.location_address'
        db.alter_column('publicity_event', 'location_address', self.gf('django.db.models.fields.CharField')(default='', max_length=100))

        # Changing field 'Event.duration_hours'
        db.alter_column('publicity_event', 'duration_hours', self.gf('django.db.models.fields.FloatField')(default=''))


    models = {
        'publicity.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'duration_hours': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location_directions': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['publicity']
