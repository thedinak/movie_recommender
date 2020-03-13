import random
import pickle
from collections import defaultdict
import numpy as np

NMF_Q = pickle.load( open( "NMF_Q.pickle", "rb" ) )
NMF_model = pickle.load( open( "NMF_model.pickle", "rb" ) )
NMF_P = pickle.load( open( "NMF_P.pickle", "rb" ) )
movies_list = pickle.load(open("movies_list.pickle", 'rb'))
#steps to take:
# 1. impute 2.5 for unknown values from user:
def convert_user_info(user_movies):
    it = iter(user_movies)
    user_movies_dict = dict(zip(it, it))
    original_values = {k:float(v) for k,v in user_movies_dict.items()}
    return original_values

def get_rhat_user(original_values, movies_list, NMF_model, NMF_Q):
    user_values_array =  np.asarray([original_values[movie] if movie in original_values.keys() else 0 for movie in movies_list])
    user_P = NMF_model.transform(user_values_array.reshape(1,-1))
    user_rhat = np.dot(user_P, NMF_Q)
    return user_rhat

def get_user_prediction_dict(movies_list, user_rhat):
    user_dict=dict(zip(movies_list,user_rhat[0]))
    user_pred_dict = defaultdict(list)
    {user_pred_dict[v].append(k) for k, v in user_dict.items()}
    return user_pred_dict

def get_movie_names(n, user_rhat, user_pred_dict, original_values):
    pred_sorted = np.sort(user_rhat)[0][::-1]
    movies_sorted = [] #list of lists
    sugg_movies = []
    for i in range(n*2):
        movies_sorted.append(user_pred_dict[pred_sorted[i]])
    print(movies_sorted)
    for movies_list in movies_sorted:
        for movie in movies_list:
            if len(sugg_movies)<n and movie not in sugg_movies and movie not in original_values.keys():
                sugg_movies.append(movie)
    return sugg_movies

def get_full_prediction(n, user_movies, movies_list, NMF_model, NMF_Q):
    original_values = convert_user_info(user_movies)
    user_rhat = get_rhat_user(original_values, movies_list, NMF_model, NMF_Q)
    user_pred_dict = get_user_prediction_dict(movies_list, user_rhat)
    sugg_movies = get_movie_names(n, user_rhat, user_pred_dict, original_values)
    return sugg_movies
