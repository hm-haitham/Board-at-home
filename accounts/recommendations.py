import numpy as np
from django.db import connection
from operator import itemgetter
from django.shortcuts import render

# Returns a dict {"CategoryName" : avg rating in category} for each game in a users wishlist, owned list or liked list
def category_avg_rating_map(cursor):
    categories = {}
    counts = {}
    for row in cursor.fetchall():
        for e in row[0].split(","):
            if e in categories:
                counts[e] += 1
                categories[e] += row[1]
            else:
                counts[e] = 1
                categories[e] = row[1]
    for category in categories:
        categories[category] /= counts[category]
    return categories # Returns dict {"CategoryName" : avg rating in category}

# Vector with category name - index mapping used to for feature construction
def get_category_mapping():
    with connection.cursor() as cursor:
        cursor.execute("SELECT Category FROM games WHERE Name NOT NULL;")
        categories = set()
        for row in cursor.fetchall():
            for e in row[0].split(","):
                categories.add(e)
        return {v:k for k, v in enumerate(categories)} # Returns dict {"CategoryName" : index}

# Returns a vector v containing the average score of the games in a users wishlist, owned list or liked list of a given
# category. Component v_i denotes the average score of the games of category at index i in category mapping for a specfic
# user
def get_user_category_vector(userID):
    with connection.cursor() as cursor:
        cursor.execute( "SELECT g1.Category, g2.Score " +
                        "FROM games g1, " +
                            "(SELECT Game_ID, Score From Relation " +
                             "Where User_ID = " + str(userID) +
                                    " And (Score >= 3 OR Owned=True OR Wishlist=True) And Score NOT NULL) g2 " +
                        "WHERE (g1.Name NOT NULL) And g1.Game_ID = g2.Game_ID;")
        user_categories = category_avg_rating_map(cursor) # dict {"CategoryName" : avg rating in category}
        category_mapping = get_category_mapping() # dict {"CategoryName" : index}
        category_vector = np.zeros(len(category_mapping))
        for category in user_categories:
            category_vector[category_mapping[category]] = user_categories[category]
        return np.array(category_vector)

# In database creates table Game_Category_Vectors that contains the item based game category vectors
def create_table_game_category_vector():
    with connection.cursor() as cursor:
        cursor.execute("SELECT Category, Rating FROM games WHERE Name NOT NULL;")
        game_category_vectors = []
        category_mapping = get_category_mapping() # dict {"CategoryName" : index}
        v_len = len(category_mapping)
        max_score = max(cursor.fetchall(), key=itemgetter(1))[1]
        cursor.execute("SELECT Category, Rating FROM games WHERE Name NOT NULL;")
        for row in cursor.fetchall():
            category_vector = np.zeros(v_len)
            for category in row[0].split(","):
                category_vector[category_mapping[category]] += 1
            category_vector *= row[1] / float(max_score)                 # pas sur que reduction de taille soit necessaire
            game_category_vectors.append(np.array(category_vector))
        game_category_vectors = np.array(game_category_vectors)
        query = ""
        for i in range(v_len):
            if i != v_len-1:
                query += "id" + str(i) + " FLOAT, "
            else:
                query += "id" + str(i) + " FLOAT"
        cursor.execute("Create Table Game_Category_Vectors (" + query + ");")
        for i in range(len(game_category_vectors)): # for all games
            query = "("
            for j in range(len(game_category_vectors[0])): # for all categories
                if j == len(game_category_vectors[0]) - 1:
                    query += str(game_category_vectors[i][j])
                else:
                    query += str(game_category_vectors[i][j]) + ", "
            query += ");"
            print (query)
            cursor.execute("Insert Into Game_Category_Vectors Values " + query)
        return np.array(game_category_vectors)

# Read game category vectors in databaase
def get_game_category_vector():
    with connection.cursor() as cursor:
        game_category_vectors = []
        cursor.execute("SELECT * FROM Game_Category_Vectors;")
        for row in cursor.fetchall():
            print (row)
            game_category_vectors.append(np.array(row))
        return np.array(game_category_vectors)

# Given index of category return name
def get_name_from_index(index):
    if 0 <= index <= 82:
        category_mapping = get_category_mapping()
        for k in category_mapping:
            if category_mapping[k] == index:
                return k
    else:
        print ("Invalid index")
        raise Exception()

def recommendations(request):
    cat_vec = get_user_category_vector(6)
    # create_table_game_category_vector()
    game_cat_vec = get_game_category_vector()
    # print ("Category vector " + str(game_cat_vec))
    # args = {"game_cat_vec": game_cat_vec}
    return render(request, "accounts/recommendations.html")
