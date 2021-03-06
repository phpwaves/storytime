# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Line'
        db.create_table(u'story_line', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'story', ['Line'])

        # Adding model 'ZomatoItem'
        db.create_table(u'story_zomatoitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('recommendations', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rating_scale', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('rating_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('highlights', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cuisines', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('opening_times', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('happy_hours', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('cost', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('buffet', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('images', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'story', ['ZomatoItem'])

        # Adding model 'user_profile'
        db.create_table(u'story_user_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('restaurants', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_night', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('family_dinner', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('on_a_Budget', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('video_games', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('xbox', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('PS', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('PC', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('gender', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('shopping', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('best_deals', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('daily_picks', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('art', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('art_galleries', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('design', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('technology', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('latest_phones', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('electronics', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('mobile_phones', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tvs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('home_theater', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fashion', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clothes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('accessories', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('shoes', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('clubs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dance_clubs', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('bars', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sports_bars', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('dive_bars', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pubs', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'story', ['user_profile'])


    def backwards(self, orm):
        # Deleting model 'Line'
        db.delete_table(u'story_line')

        # Deleting model 'ZomatoItem'
        db.delete_table(u'story_zomatoitem')

        # Deleting model 'user_profile'
        db.delete_table(u'story_user_profile')


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
        u'story.line': {
            'Meta': {'object_name': 'Line'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'story.user_profile': {
            'Meta': {'object_name': 'user_profile'},
            'PC': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'PS': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'accessories': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'art': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'art_galleries': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'bars': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'best_deals': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clothes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'clubs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'daily_picks': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dance_clubs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_night': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'design': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'dive_bars': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'electronics': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family_dinner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fashion': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gender': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'home_theater': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_phones': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'mobile_phones': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'on_a_Budget': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pubs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'restaurants': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shoes': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shopping': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sports_bars': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'technology': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tvs': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'video_games': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'xbox': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'story.zomatoitem': {
            'Meta': {'object_name': 'ZomatoItem'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'area': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'buffet': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cuisines': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'happy_hours': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'highlights': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'opening_times': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rating_scale': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'rating_value': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recommendations': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['story']