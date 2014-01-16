# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Exercise'
        db.create_table(u'exerciselibrary_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('muscle', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('level', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('exercise_place', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('home_gym', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('order', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'exerciselibrary', ['Exercise'])

        # Adding model 'ExerciseImage'
        db.create_table(u'exerciselibrary_exerciseimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exerciselibrary.Exercise'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('featured_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'exerciselibrary', ['ExerciseImage'])

        # Adding model 'Tag'
        db.create_table(u'exerciselibrary_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('exercise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exerciselibrary.Exercise'])),
            ('tag', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'exerciselibrary', ['Tag'])

        # Adding model 'Category'
        db.create_table(u'exerciselibrary_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'exerciselibrary', ['Category'])

        # Adding M2M table for field exercises on 'Category'
        m2m_table_name = db.shorten_name(u'exerciselibrary_category_exercises')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'exerciselibrary.category'], null=False)),
            ('exercise', models.ForeignKey(orm[u'exerciselibrary.exercise'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'exercise_id'])

        # Adding model 'CategoryImage'
        db.create_table(u'exerciselibrary_categoryimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['exerciselibrary.Category'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('featured_image', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'exerciselibrary', ['CategoryImage'])


    def backwards(self, orm):
        # Deleting model 'Exercise'
        db.delete_table(u'exerciselibrary_exercise')

        # Deleting model 'ExerciseImage'
        db.delete_table(u'exerciselibrary_exerciseimage')

        # Deleting model 'Tag'
        db.delete_table(u'exerciselibrary_tag')

        # Deleting model 'Category'
        db.delete_table(u'exerciselibrary_category')

        # Removing M2M table for field exercises on 'Category'
        db.delete_table(db.shorten_name(u'exerciselibrary_category_exercises'))

        # Deleting model 'CategoryImage'
        db.delete_table(u'exerciselibrary_categoryimage')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'exerciselibrary.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'exercises': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['exerciselibrary.Exercise']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'exerciselibrary.categoryimage': {
            'Meta': {'object_name': 'CategoryImage'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exerciselibrary.Category']"}),
            'featured_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'exerciselibrary.exercise': {
            'Meta': {'ordering': "['-order']", 'object_name': 'Exercise'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'exercise_place': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'home_gym': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'muscle': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'exerciselibrary.exerciseimage': {
            'Meta': {'object_name': 'ExerciseImage'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exerciselibrary.Exercise']"}),
            'featured_image': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'exerciselibrary.tag': {
            'Meta': {'object_name': 'Tag'},
            'exercise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['exerciselibrary.Exercise']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['exerciselibrary']