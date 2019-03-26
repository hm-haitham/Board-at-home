# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse, Http404
from django.shortcuts import render
from django.db import connection
import unicodedata

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def get_games_sql():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM games WHERE Name NOT NULL;")
        games_rows = dictfetchall(cursor)	#[{'Game_ID': 1, 'Description': "...", Image:"...", ...}, {'Game_ID': 2, 'Description': "...", Image:"..."}...]
        # cursor.execute("SELECT * FROM Users;")
        # user_rows = dictfetchall(cursor)
        # cursor.execute("SELECT * FROM Relation;")
        # relation_rows = dictfetchall(cursor)
    return games_rows

def get_game_sql(game_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM games WHERE Game_ID=" + str(game_id) + ";")
        game_rows = dictfetchall(cursor)	#[{'Game_ID': 1, 'Description': "...", Image:"...", ...}, {'Game_ID': 2, 'Description': "...", Image:"..."}...]
        # cursor.execute("SELECT * FROM Users;")
        # user_rows = dictfetchall(cursor)
        # cursor.execute("SELECT * FROM Relation;")
        # relation_rows = dictfetchall(cursor)
    return game_rows[0]

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

def index(request):
    games = get_games_sql()
    return render(request, 'Game/index.html', {'games': games})

def detail(request, game_id):
    game = get_game_sql(game_id)
    if not game:
        raise Http404("Game does not exist")
    return render(request, "Game/detail.html", {'game': game, 'user': request.user})
