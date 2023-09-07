import flask
import json
from flask import Flask, jsonify, render_template, request, redirect, url_for, session, flash
app = Flask(__name__)

# Specify the path to your JSON file

# Open the JSON file for reading
with open("data1.json", "r") as json_file: 
    # Parse the JSON data into a Python data structure
    data = json.load(json_file)

@app.route('/news/<string:category>')   
def news(category):
    if category=="sports":
        # Return the JSON data as a Python dictionary to the endpoint
        return data  

@app.route("/news/sports/<int:count>")
def get_news_count(count):
    if count<=len(data):
        response_news = [data[i] for i in range(count)]
        return jsonify({'news': response_news})
    else:
        return jsonify({'error': 'Data not found'})
if __name__ ==  '__main__':
    app.run(debug=True)
