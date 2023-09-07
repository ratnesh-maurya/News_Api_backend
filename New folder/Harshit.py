import json
from flask import Flask,request,jsonify

app=Flask(__name__)
#C:\Harshit\Python\Api project\
filename="data.json"
with open(filename) as json_file:
    Education_data = json.load(json_file)
# print(data)

@app.route("/news")

def home():
     return Education_data
    
@app.route("/news/<int:count>")

def get_news_count(count):
    print(len(Education_data))
    if count<=len(Education_data):
        response_news= [Education_data[i] for i in range(count) ]
        return jsonify({'news':response_news})
    else:
        return jsonify({'message':'Not enough news articles available'})



if __name__=="__main__":
    app.run(debug=True)