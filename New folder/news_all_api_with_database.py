from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
import json

import pymongo

app = Flask(__name__)

# connect to mongodb
connection_string = "mongodb+srv://ratnesh:ratnesh@cluster0.3ka0uom.mongodb.net/"

# Establish a connection to the MongoDB Atlas cluster
client = pymongo.MongoClient(connection_string)


# connect to database
db = client['news_database']

# connect to collection
news = db['news_collection']
crime_news = db['crime_news_collection']
sports_news = db['sports_news_collection']


# Convert ObjectId to string in JSON response
def jsonify_with_objectid(data):
    return jsonify(json.loads(dumps(data, default=str)))


# Get all news articles
@app.route('/news', methods=['GET'])
def get_all_news():
    return jsonify_with_objectid(news.find())


# Get a specific number of news articles
@app.route('/news/<int:count>', methods=['GET'])
def get_news_count(count):
    news_list = list(news.find().limit(count))
    return jsonify_with_objectid(news_list)


# Get all crime news articles
@app.route('/news/crime', methods=['GET'])
def get_all_crime_news():
    return jsonify_with_objectid(crime_news.find())


# Get a specific number of crime news articles
@app.route('/news/crime/<int:count>', methods=['GET'])
def get_crime_news_count(count):
    crime_news_list = list(crime_news.find().limit(count))
    return jsonify_with_objectid(crime_news_list)


# Get all sports news articles
@app.route('/news/sports', methods=['GET'])
def get_all_sports_news():
    return jsonify_with_objectid(sports_news.find())


# Get a specific number of sports news articles
@app.route('/news/sports/<int:count>', methods=['GET'])
def get_sports_news_count(count):
    sports_news_list = list(sports_news.find().limit(count))
    return jsonify_with_objectid(sports_news_list)


if __name__ == "__main__":
    app.run(debug=True)
