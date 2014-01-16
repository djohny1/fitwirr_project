# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'News.slug'
        db.alter_column(u'press_news', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'News.slug'
        raise RuntimeError("Cannot reverse this migration. 'News.slug' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'News.slug'
        db.alter_column(u'press_news', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50))

    models = {
        u'press.news': {
            'Meta': {'object_name': 'News'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'sub_headline': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
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