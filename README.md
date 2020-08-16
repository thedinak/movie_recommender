# movie_recommender
Movie recommender implemented through Flask, based on collaborative filtering.

## Features
* Collaborative filtering (**non-negative factorisation**, NMF) with scikit-learn to make recommendations;
* Flask web-interface;
* CSS from Bootstrap;

# How to run:
1. Clone the repository `git clone https://github.com/thedinak/movie_recommender.git`

2. Go into the folder `cd movie_recommender`

3. Install requirements `pip install -r requirements.txt`

4. Set environment variable 'export FLASK_APP=webserver.py'

5. Start Flask server 'flask run'

6. Go to http://127.0.0.1:5000/
