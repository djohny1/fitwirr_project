# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'News'
        db.create_table(u'press_news', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'press', ['News'])

        # Adding model 'NewsImage'
        db.create_table(u'press_newsimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('news', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['press.News'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'press', ['NewsImage'])


    def backwards(self, orm):
        # Deleting model 'News'
        db.delete_table(u'press_news')

        # Deleting model 'NewsImage'
        db.delete_table(u'press_newsimage')


    models = {
        u'press.news': {
            'Meta': {'object_name': 'News'},
            'content': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
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