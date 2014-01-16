# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Author'
        db.delete_table(u'blog_author')

        # Deleting model 'Post'
        db.delete_table(u'blog_post')

        # Adding model 'Blog'
        db.create_table(u'blog_blog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('posted', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'blog', ['Blog'])

        # Adding M2M table for field category on 'Blog'
        m2m_table_name = db.shorten_name(u'blog_blog_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('blog', models.ForeignKey(orm[u'blog.blog'], null=False)),
            ('category', models.ForeignKey(orm[u'blog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['blog_id', 'category_id'])

        # Adding model 'Category'
        db.create_table(u'blog_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
        ))
        db.send_create_signal(u'blog', ['Category'])

        # Deleting field 'Comment.post'
        db.delete_column(u'blog_comment', 'post_id')

        # Adding field 'Comment.blog'
        db.add_column(u'blog_comment', 'blog',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=2, to=orm['blog.Blog']),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Author'
        db.create_table(u'blog_author', (
            ('profile_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'blog', ['Author'])

        # Adding model 'Post'
        db.create_table(u'blog_post', (
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('body_content', self.gf('django.db.models.fields.TextField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Author'])),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=100, unique=True)),
        ))
        db.send_create_signal(u'blog', ['Post'])

        # Deleting model 'Blog'
        db.delete_table(u'blog_blog')

        # Removing M2M table for field category on 'Blog'
        db.delete_table(db.shorten_name(u'blog_blog_category'))

        # Deleting model 'Category'
        db.delete_table(u'blog_category')


        # User chose to not deal with backwards NULL issues for 'Comment.post'
        raise RuntimeError("Cannot reverse this migration. 'Comment.post' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Comment.post'
        db.add_column(u'blog_comment', 'post',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Post']),
                      keep_default=False)

        # Deleting field 'Comment.blog'
        db.delete_column(u'blog_comment', 'blog_id')


    models = {
        u'blog.blog': {
            'Meta': {'object_name': 'Blog'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['blog.Category']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blog.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'blog.comment': {
            'Meta': {'object_name': 'Comment'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'blog': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['blog.Blog']"}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['blog']