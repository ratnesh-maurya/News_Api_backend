from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open("news_data_crime.json") as f:
    crime_news = json.load(f)

# Get all news articles


@app.route('/news/crime', methods=['GET'])
def get_all_news():
    return jsonify({'news': crime_news})

# Get a specific number of news articles (specified by count)


@app.route('/news/crime/<int:count>', methods=['GET'])
def get_news_count(count):
    print(len(crime_news))
    if count <= len(crime_news):
        response_news = [crime_news[i] for i in range(count)]
        return jsonify({'news': response_news})
    else:
        return jsonify({'message': 'Not enough news articles available'}), 404


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
