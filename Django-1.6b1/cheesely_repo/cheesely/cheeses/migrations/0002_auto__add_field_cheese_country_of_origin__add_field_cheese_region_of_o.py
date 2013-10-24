# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Cheese.country_of_origin'
        db.add_column(u'cheeses_cheese', 'country_of_origin',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Cheese.region_of_origin'
        db.add_column(u'cheeses_cheese', 'region_of_origin',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Cheese.country_of_origin'
        db.delete_column(u'cheeses_cheese', 'country_of_origin')

        # Deleting field 'Cheese.region_of_origin'
        db.delete_column(u'cheeses_cheese', 'region_of_origin')


    models = {
        u'cheeses.cheese': {
            'Meta': {'object_name': 'Cheese'},
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'firmness': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'region_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cheeses']