from flask import Flask, request, render_template, Blueprint, redirect, url_for

from src.service.search_service import search_tweet

second = Blueprint("second", __name__, template_folder="templates", static_folder="static")

@second.route('/')
def hello():
    return render_template('index.html')

@second.route('/search', methods=['POST'])
def search_controller():
    search_name = request.form['search_name']
#   print(search_name)
    tweets = search_tweet(search_name)
    for tweet in tweets:
        print()
    return render_template('index.html', tweets=tweets)
