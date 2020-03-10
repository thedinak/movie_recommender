import random

def get_recommendation(k=1):
    movies= ['Parasite', 'Knives Out', 'some movie', 'a different movie', 'aww', 'look up here cat!']
    return random.choices(movies, k=k)
