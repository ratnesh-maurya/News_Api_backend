
from flask import Flask,jsonify
from pymongo import MongoClient
from bson.json_util import dumps
from pymongo import MongoClient
from bson import json_util
import json
import requests
                                                 
app=Flask(__name__)

#connect to mongodb
client = MongoClient('localhost', 27017)

#connect to database
db = client['news_database']

#connect to collection
news = db['news_collection']
crime_news = db['crime_news_collection']
sports_news = db['sports_news_collection'] 

# Get all news articles
@app.route('/news',methods=['GET'])
def home():
    return jsonify(dumps(news.find()))
   

@app.route('/news/<int:count>',methods=['GET'])

def get_news_count(count):
    if count<=news.count():
        response_news= [news.find()[i] for i in range(count) ]
        return jsonify({'news':response_news})
    else:
        return jsonify({'message':'Not enough news articles available'})
    
    

# Get all crime news articles
@app.route('/news/crime', methods=['GET'])
def get_crime_news():
    return dumps(crime_news.find())

@app.route('/news/crime/<int:count>',methods=['GET'])

def get_crime_news_count(count):
    if count<=crime_news.count():
        response_news= [crime_news.find()[i] for i in range(count) ]
        return jsonify({'news':response_news})
    else:
        return jsonify({'message':'Not enough crime news articles available'})
    

# Get all sports news articles
@app.route('/news/sports', methods=['GET'])
def get_sports_news():
    return dumps(sports_news.find())

@app.route('/news/sports/<int:count>',methods=['GET'])

def get_sports_news_count(count):
    if count<=sports_news.count():
        response_news= [sports_news.find()[i] for i in range(count) ]
        return jsonify({'news':response_news})
    else:
        return jsonify({'message':'Not enough sports news articles available'})



if __name__=="__main__":
    app.run(debug=True)
