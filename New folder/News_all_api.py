import json
from flask import Flask,request,jsonify



app=Flask(__name__)


with open("news_data.json") as json_file:
    news_data = json.load(json_file)

with open("news_data_crime.json") as f:
    crime_news = json.load(f)

with open("news_data_Sports.json") as r:
    sports_data=json.load(r)

#######################################################################################################

# Get all news articles
@app.route('/news',methods=['GET'])

def home():
     return news_data
    
@app.route('/news/<int:count>',methods=['GET'])

def get_news_count(count):
    print(len(news_data))
    if count<=len(news_data):
        response_news= [news_data[i] for i in range(count) ]
        return jsonify({'news':response_news})
    else:
        return jsonify({'message':'Not enough news articles available'})
    
#######################################################################################################

# Get all crime news articles
@app.route('/news/crime', methods=['GET'])
def get_all_news():
    return jsonify({'news': crime_news})

# Get a specific number of news articles (specified by count)


@app.route('/news/crime/<int:count>', methods=['GET'])
def get_news_count_crime(count):
    print(len(crime_news))
    if count <= len(crime_news):
        response_news = [crime_news[i] for i in range(count)]
        return jsonify({'news': response_news})
    else:
        return jsonify({'message': 'Not enough news articles available'}), 404

#######################################################################################################

@app.route('/news/<string:category>')

def news(category):
    if category == "sports":
        return jsonify({'news': sports_data})  # Return the entire JSON data for the "sports" category
#new route for educatrion 

@app.route("/news/sports/<int:count>")
def get_news_count_sports(count):
    if count <= len(sports_data):
        response_news = []
        for i in range(count):
            response_news.append(sports_data[i])
        return jsonify({'news': response_news})
    else:
        return jsonify({'error': 'Data not found'})
    
#######################################################################################################

if __name__=="__main__":
    app.run(debug=True)