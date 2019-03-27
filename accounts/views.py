from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import RegistrationForm, UserProfileForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# Create your views here.


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
        cursor.execute("SELECT Name FROM Relation Where Wishlist=true and User_ID=" + str(request.user.id))
        result = dictfetchall(cursor)
    return result

# Retreive the names of the Games in wishlist from database
def view_ownedlist(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT Name FROM Relation Where Owned=true and User_ID=" + str(request.user.id))
        result = dictfetchall(cursor)
    return result

def get_game_sql(game_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM games WHERE Game_ID=" + str(game_id) + ";")
        game_rows = dictfetchall(cursor)	#[{'Game_ID': 1, 'Description': "...", Image:"...", ...}, {'Game_ID': 2, 'Description': "...", Image:"..."}...]
    return game_rows[0]

# Remove the names of the Games in wishlist from database
def remove_from_wishlist(request, game_id):
    with connection.cursor() as cursor:
        result = get_game_sql(game_id)
        if result["Owned"]:
            cursor.execute("UPDATE Relation SET Wishlist=false WHERE User_ID="
                           + str(request.user.id) + " AND Game_ID=" + str(game_id))
        else:
            cursor.execute("DELETE FROM Relation Where Game_ID=" + str(game_id) +
                           " and User_ID=" + str(request.user.id))
    return result

# Remove the names of the Games in wishlist from database
def view_ownedlist(request):
    with connection.cursor() as cursor:
        result = get_game_sql(game_id)
        if result["Wishlist"]:
            cursor.execute("UPDATE Relation SET Owned=false WHERE User_ID="
                           + str(request.user.id) + " AND Game_ID=" + str(game_id))
        else:
            cursor.execute("DELETE FROM Relation Where Game_ID=" + str(game_id) +
                           " and User_ID=" + str(request.user.id))
    return result


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


def search(request):
    return render(request, "accounts/Search_Page.html")



def view_profile(request):
    args ={'user': request.user}
    return render(request, "accounts/profile.html", args)

def about(request):
    return render(request, "accounts/about.html")




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
