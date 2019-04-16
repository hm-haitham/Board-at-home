from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import RegistrationForm, UserProfileForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.db import connection
from django.http import HttpResponseRedirect
import random
from . import recommendations



def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# Retreive the names of the Games in wishlist from database
def view_wishlist(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Game_ID, Score FROM Relation Where Wishlist=true and User_ID=" + str(request.user.id))
        result = dictfetchall(cursor)
    return result

# Retreive the names of the Games in wishlist from database
def view_ownedlist(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Game_ID, Score FROM Relation Where Owned=true and User_ID=" + str(request.user.id))
        result = dictfetchall(cursor)
    return result

def get_game_sql(game_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM games WHERE Game_ID=" + str(game_id) + ";")
        game_rows = dictfetchall(cursor)	#[{'Game_ID': 1, 'Description': "...", Image:"...", ...}, {'Game_ID': 2, 'Description': "...", Image:"..."}...]
    return game_rows[0]

def get_relation_sql(game_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Relation WHERE Game_ID=" + str(game_id) + ";")
        game_rows = dictfetchall(cursor)
    return game_rows[0]


#Get the first name, zip code, and email of people  who own a game on your Wishlist

def wishlist_owned_finder(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * \
        FROM ((SELECT User_id AS wisher_id, Game_ID FROM Relation WHERE Wishlist = TRUE AND user_id=" + str(request.user.id) + ") O \
        NATURAL JOIN (SELECT user_id AS wisher_id, zipcode as wisher_zipcode FROM accounts_userprofile) E ) \
        NATURAL JOIN  (SELECT name, Game_ID FROM games) \
        NATURAL JOIN \
        (((SELECT user_id as id, Game_ID FROM Relation WHERE Owned=TRUE AND user_id !=" + str(request.user.id) + ") B \
        NATURAL JOIN auth_user ) C \
        NATURAL JOIN ( SELECT zipcode as owner_zipcode, user_id AS id FROM accounts_userprofile) D) E \
        WHERE (substr(cast(wisher_zipcode as varchar),1,3)) = (substr(cast(owner_zipcode as varchar),1,3)) ")

        result = dictfetchall(cursor)
    return result


def find_nearby_players(request):
    result = {"result": wishlist_owned_finder(request)}
    return render(request, "accounts/nearby_players.html",result)

# Remove the names of the Games in wishlist from database
def remove_from_wishlist(request, game_id):
    with connection.cursor() as cursor:
        result = get_relation_sql(game_id)
        if result["Owned"]:
            cursor.execute("UPDATE Relation SET Wishlist=false WHERE User_ID="
                           + str(request.user.id) + " AND Game_ID=" + str(game_id))
        else:
            cursor.execute("DELETE FROM Relation Where Game_ID=" + str(game_id) +
                           " and User_ID=" + str(request.user.id))
    wishlist = view_wishlist(request)
    print (wishlist)
    wishlist_games = []
    for e in wishlist:
        wishlist_games.append(get_game_sql(e["Game_ID"]))
    ownedlist = view_ownedlist(request)
    ownedlist_games = []
    for e in ownedlist:
        ownedlist_games.append(get_game_sql(e["Game_ID"]))
    args = {'user': request.user, 'wishlist_games': wishlist_games, 'ownedlist_games': ownedlist_games}
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), args)

# Remove the names of the Games in wishlist from database
def remove_from_ownedlist(request, game_id):
    with connection.cursor() as cursor:
        result = get_relation_sql(game_id)
        if result["Wishlist"]:
            cursor.execute("UPDATE Relation SET Owned=false WHERE User_ID="
                           + str(request.user.id) + " AND Game_ID=" + str(game_id))
        else:
            cursor.execute("DELETE FROM Relation Where Game_ID=" + str(game_id) +
                           " and User_ID=" + str(request.user.id))
    wishlist = view_wishlist(request)
    print (wishlist)
    wishlist_games = []
    for e in wishlist:
        wishlist_games.append(get_game_sql(e["Game_ID"]))
    ownedlist = view_ownedlist(request)
    ownedlist_games = []
    for e in ownedlist:
        ownedlist_games.append(get_game_sql(e["Game_ID"]))
    args = {'user': request.user, 'wishlist_games': wishlist_games, 'ownedlist_games': ownedlist_games}
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), args)

def home(request):
    numbers = [1,2,3,4,5]
    name = "Julius Pasion"
    args = {'myName': name,'numbers' : numbers }
    return render(request, "accounts/home.html", args)

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

        return redirect('/accounts')
    else:
        form = RegistrationForm()
        profile_form = UserProfileForm()

        args = {'form':form, 'profile_form': profile_form}
        return render(request,'accounts/reg_form.html', args)


def search_game_sql(name,category,players):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM games WHERE Name LIKE '%" + str(name) + "%' AND Category LIKE '%" + str(category) + "%' AND Min_players = " + str(players) + ";")
        game_rows = dictfetchall(cursor)	#[{'Game_ID': 1, 'Description': "...", Image:"...", ...}, {'Game_ID': 2, 'Description': "...", Image:"..."}...]
    return game_rows

def search(request):
    if request.method=='POST':
        srch = request.POST['srh']
        srch2 = request.POST['srh2']
        srch3 = request.POST['srh3']
        if srch3:
            if (srch or srch2 or srch3):
                games = search_game_sql(srch,srch2,srch3)
                if games:
                    return render(request, "accounts/Search_Page.html", {'games': games})
            else:
                return HttpResponseRedirect('/accounts/search/')
        else:
            if (srch or srch2):
                games = search_game_sql(srch,srch2,'Min_players')
                if games:
                    return render(request, "accounts/Search_Page.html", {'games': games})
            else:
                return HttpResponseRedirect('/accounts/search/')  
    return render(request, 'accounts/Search_Page.html')


def view_profile(request):
    wishlist = view_wishlist(request)
    wishlist_games = []
    for e in wishlist:
        wishlist_games.append([get_game_sql(e["Game_ID"]), e["Score"]])
    ownedlist = view_ownedlist(request)
    ownedlist_games = []
    for e in ownedlist:
        ownedlist_games.append([get_game_sql(e["Game_ID"]), e["Score"]])
    user_based_recommendations = recommendations.user_based_recommendations(request)
    print ("user_based_recommendations " + str(user_based_recommendations) )
    args = {'user': request.user, 'wishlist_games': wishlist_games,
            'ownedlist_games': ownedlist_games, 'user_based_recommendations': user_based_recommendations}
    return render(request, "accounts/profile.html", args)


def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')

    else:
        form = EditProfileForm(instance =request.user)
        args = {'form': form}
        return render(request,"accounts/edit_profile.html", args)

def about(request):
    return render(request, "accounts/about.html")

def get_random_game(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM games ;")
        game_rows = dictfetchall(cursor)	#[{'Game_ID': 1, 'Description': "...", Image:"...", ...}, {'Game_ID': 2, 'Description': "...", Image:"..."}...]
        game= random.choice(game_rows)
        if not game:
            raise Http404("Game does not exist")
    return HttpResponseRedirect('/games/'+str(game["Game_ID"]), {'game': game, 'user': request.user})
    # return render(request, "Game/detail.html", {'game': game, 'user': request.user})
