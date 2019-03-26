# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
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
