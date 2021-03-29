from flask import request, render_template, Blueprint

from search import search_tweet

second = Blueprint("second", __name__, template_folder="templates", static_folder="static")

@second.route('/')
def hello():
    return render_template('index.html')

@second.route('/search', methods=['POST'])
def search_controller():
    search_name = request.form['search_name']
    tweets = search_tweet(search_name)
    return render_template('index.html', tweets=tweets)
