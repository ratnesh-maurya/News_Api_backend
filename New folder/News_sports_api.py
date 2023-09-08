import json
from flask import Flask, jsonify

app = Flask(__name__)

# Define the path to your JSON file
json_file_path = "news_data_Sports"

# Function to load JSON data
def load_json_data(file_path):
    try:
        with open(file_path, "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return None  # Return None if the file is not found
    except json.JSONDecodeError:
        return None  # Return None if there's an issue decoding JSON

# Load JSON data into a variable
data = load_json_data(json_file_path)

# Check if data is loaded successfully
if data is None:
    raise Exception("Failed to load JSON data")

@app.route('/news/<string:category>')

def news(category):
    if category == "sports":
        return jsonify({'news': data})  # Return the entire JSON data for the "sports" category
#new route for educatrion 

@app.route("/news/sports/<int:count>")
def get_news_count(count):
    if count <= len(data):
        response_news = []
        for i in range(count):
            response_news.append(data[i])
        return jsonify({'news': response_news})
    else:
        return jsonify({'error': 'Data not found'})

if __name__ == '__main__':
    app.run(debug=True)
