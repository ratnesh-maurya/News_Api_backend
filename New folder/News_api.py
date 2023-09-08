import json
from flask import Flask,request,jsonify

#add comments 

app=Flask(__name__)

filename="news_data.json"
with open(filename) as json_file:
    news_data = json.load(json_file)

@app.route("/news")

def home():
     return news_data
    
@app.route("/news/<int:count>")

def get_news_count(count):
    print(len(news_data))
    if count<=len(news_data):
        response_news= [news_data[i] for i in range(count) ]
        return jsonify({'news':response_news})
    else:
        return jsonify({'message':'Not enough news articles available'})



if __name__=="__main__":
    app.run(debug=True)