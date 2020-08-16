from flask import Flask
from flask import render_template
from flask import request
import recommender
import pickle
from collections import defaultdict

NMF_Q = pickle.load(open("NMF_Q.pickle", "rb"))
NMF_model = pickle.load(open("NMF_model.pickle", "rb"))
NMF_P = pickle.load(open("NMF_P.pickle", "rb"))
movies_list = pickle.load(open("movies_list.pickle", 'rb'))

app = Flask('_name_')


@app.route('/')  # connect to actual html
def hello():
    return render_template('main_page.html')


@app.route('/recommend', methods=['POST'])
def run_recommender():
    n = int(request.form['n_movies'])
    user_movies = (request.form['user_movies']).split(',')
    result = recommender.get_full_prediction(n, user_movies, movies_list,
                                             NMF_model, NMF_Q)

    context = dict(title='TITLE GOES HERE', movies=result)
    return render_template('recommendation.html', **context)


@app.route('/full_movie_list', methods=['GET'])
def import_movie_list():
    context = dict(movies_names=movies_list)
    return render_template('full_movie_list.html', **context)
