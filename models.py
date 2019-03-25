# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Games(models.Model):
    game_id = models.IntegerField(db_column='Game_ID')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    max_players = models.IntegerField(db_column='Max_players', blank=True, null=True)  # Field name made lowercase.
    min_age = models.IntegerField(db_column='Min_age', blank=True, null=True)  # Field name made lowercase.
    min_players = models.IntegerField(db_column='Min_players', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    playing_time = models.IntegerField(db_column='Playing_time', blank=True, null=True)  # Field name made lowercase.
    year_published = models.IntegerField(db_column='Year_published', blank=True, null=True)  # Field name made lowercase.
    boardgame_artist = models.TextField(db_column='Boardgame_artist', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    designer = models.TextField(db_column='Designer', blank=True, null=True)  # Field name made lowercase.
    boardgame_family = models.TextField(db_column='Boardgame_family', blank=True, null=True)  # Field name made lowercase.
    implementation = models.TextField(db_column='Implementation', blank=True, null=True)  # Field name made lowercase.
    integration = models.TextField(db_column='Integration', blank=True, null=True)  # Field name made lowercase.
    mechanics = models.TextField(db_column='Mechanics', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(db_column='Publisher', blank=True, null=True)  # Field name made lowercase.
    rating = models.FloatField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    language_dependence = models.TextField(db_column='Language_dependence', blank=True, null=True)  # Field name made lowercase.
    suggested_numplayers_1 = models.TextField(db_column='Suggested_numplayers.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_10 = models.TextField(db_column='Suggested_numplayers.10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_2 = models.TextField(db_column='Suggested_numplayers.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_3 = models.TextField(db_column='Suggested_numplayers.3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_4 = models.TextField(db_column='Suggested_numplayers.4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_5 = models.TextField(db_column='Suggested_numplayers.5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_6 = models.TextField(db_column='Suggested_numplayers.6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_7 = models.TextField(db_column='Suggested_numplayers.7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_8 = models.TextField(db_column='Suggested_numplayers.8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_9 = models.TextField(db_column='Suggested_numplayers.9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_over = models.TextField(db_column='Suggested_numplayers.Over', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_player_age = models.TextField(db_column='Suggested_player_age', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Games'


class Relation(models.Model):
    game = models.ForeignKey(Games, models.DO_NOTHING, db_column='Game_ID')  # Field name made lowercase.
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='User_ID')  # Field name made lowercase.
    owned = models.NullBooleanField(db_column='Owned')  # Field name made lowercase.
    score = models.FloatField(db_column='Score', blank=True, null=True)  # Field name made lowercase.
    review = models.TextField(db_column='Review', blank=True, null=True)  # Field name made lowercase.
    date = models.TimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    wishlist = models.NullBooleanField(db_column='Wishlist')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Relation'
        unique_together = (('game', 'user'),)


class Users(models.Model):
    user_id = models.IntegerField(db_column='User_ID')  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    zipcode = models.IntegerField(db_column='Zipcode', blank=True, null=True)  # Field name made lowercase.
    social_media = models.TextField(db_column='Social_media', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GamesGames(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    game_id = models.IntegerField(db_column='Game_ID')  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    max_players = models.IntegerField(db_column='Max_players', blank=True, null=True)  # Field name made lowercase.
    min_age = models.IntegerField(db_column='Min_age', blank=True, null=True)  # Field name made lowercase.
    min_players = models.IntegerField(db_column='Min_players', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    playing_time = models.IntegerField(db_column='Playing_time', blank=True, null=True)  # Field name made lowercase.
    year_published = models.IntegerField(db_column='Year_published', blank=True, null=True)  # Field name made lowercase.
    boardgame_artist = models.TextField(db_column='Boardgame_artist', blank=True, null=True)  # Field name made lowercase.
    category = models.TextField(db_column='Category', blank=True, null=True)  # Field name made lowercase.
    designer = models.TextField(db_column='Designer', blank=True, null=True)  # Field name made lowercase.
    boardgame_family = models.TextField(db_column='Boardgame_family', blank=True, null=True)  # Field name made lowercase.
    implementation = models.TextField(db_column='Implementation', blank=True, null=True)  # Field name made lowercase.
    integration = models.TextField(db_column='Integration', blank=True, null=True)  # Field name made lowercase.
    mechanics = models.TextField(db_column='Mechanics', blank=True, null=True)  # Field name made lowercase.
    publisher = models.TextField(db_column='Publisher', blank=True, null=True)  # Field name made lowercase.
    rating = models.FloatField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    language_dependence = models.TextField(db_column='Language_dependence', blank=True, null=True)  # Field name made lowercase.
    suggested_numplayers_1 = models.TextField(db_column='Suggested_numplayers.1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_10 = models.TextField(db_column='Suggested_numplayers.10', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_2 = models.TextField(db_column='Suggested_numplayers.2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_3 = models.TextField(db_column='Suggested_numplayers.3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_4 = models.TextField(db_column='Suggested_numplayers.4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_5 = models.TextField(db_column='Suggested_numplayers.5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_6 = models.TextField(db_column='Suggested_numplayers.6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_7 = models.TextField(db_column='Suggested_numplayers.7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_8 = models.TextField(db_column='Suggested_numplayers.8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_9 = models.TextField(db_column='Suggested_numplayers.9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_numplayers_over = models.TextField(db_column='Suggested_numplayers.Over', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    suggested_player_age = models.TextField(db_column='Suggested_player_age', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'games_games'
