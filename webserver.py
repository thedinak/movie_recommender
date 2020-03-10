from flask import Flask
from flask import render_template
from flask import request
import recommender

app = Flask('_name_')

@app.route('/') #connect to actual html #@ symbol is a decorator(adds some extra functionality to a function)
def hello():
    return render_template('main_page.html')

@app.route('/recommend', methods = ['POST']) #connect to actual html #@ symbol is a decorator(adds some extra functionality to a function)
def run_recommender():
    n = int(request.form['n_movies'])
    result= recommender.get_recommendation(n)

    context = dict(title = 'TITLE GOES HERE', movies=result)
    return render_template('recommendation.html', **context)

# @app.route('/secret')
# def get_inputs():
#     n = int(request.args['n_movies'])
#     return n
