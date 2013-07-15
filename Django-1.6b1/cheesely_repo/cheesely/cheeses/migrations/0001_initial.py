# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Cheese'
        db.create_table(u'cheeses_cheese', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('firmness', self.gf('django.db.models.fields.IntegerField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'cheeses', ['Cheese'])


    def backwards(self, orm):
        # Deleting model 'Cheese'
        db.delete_table(u'cheeses_cheese')


    models = {
        u'cheeses.cheese': {
            'Meta': {'object_name': 'Cheese'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'firmness': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['cheeses']