# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'contact_contact')


    def backwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'contact_contact', (
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'contact', ['Contact'])


    models = {
        
    }

    complete_apps = ['contact']