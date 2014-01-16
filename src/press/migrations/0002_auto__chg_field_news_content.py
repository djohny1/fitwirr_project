# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'News.content'
        db.alter_column(u'press_news', 'content', self.gf('django.db.models.fields.TextField')(max_length=500, null=True))

    def backwards(self, orm):

        # Changing field 'News.content'
        db.alter_column(u'press_news', 'content', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

    models = {
        u'press.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'press.newsimage': {
            'Meta': {'object_name': 'NewsImage'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['press.News']"})
        }
    }

    complete_apps = ['press']