# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Cheese.photo'
        db.alter_column(u'cheeses_cheese', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'Cheese.photo_attribution'
        db.alter_column(u'cheeses_cheese', 'photo_attribution', self.gf('django.db.models.fields.URLField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Cheese.photo'
        db.alter_column(u'cheeses_cheese', 'photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

        # Changing field 'Cheese.photo_attribution'
        db.alter_column(u'cheeses_cheese', 'photo_attribution', self.gf('django.db.models.fields.URLField')(max_length=255, null=True))

    models = {
        u'cheeses.cheese': {
            'Meta': {'object_name': 'Cheese'},
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'firmness': ('django.db.models.fields.IntegerField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'default': "' '", 'max_length': '100', 'blank': 'True'}),
            'photo_attribution': ('django.db.models.fields.URLField', [], {'default': "' '", 'max_length': '255', 'blank': 'True'}),
            'region_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cheeses']