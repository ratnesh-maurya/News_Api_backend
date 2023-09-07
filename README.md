
# 📰 News Backend API

This is a super cool backend API 🚀 for retrieving news articles in the categories of "crime" 🔍 and "sport" 🏆.

## 🌟 Introduction

This API provides seamless access to fascinating news articles 📝 categorized under "crime" 🔒 and "sport" 🥇. It empowers users to discover exciting news in these categories with ease. The API is ingeniously built using Flask, a Python web framework 🐍.

## ✨ Features

- Retrieve news articles in the "crime" 🔪 and "sport" 🏅 categories.
- A sleek and user-friendly RESTful API.

## 🚀 Getting Started

### Prerequisites

Before you embark on this adventure, ensure you have the following prerequisites met:

- Python 3.x installed. 🐍
- Flask library installed (you can easily install it using `pip install Flask`). 🌐

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/news-backend-api.git
   cd news-backend-api
   ```

2. Fire up the Flask application:

   ```bash
   python app.py
   ```

   Behold! The API will be accessible at `http://localhost:5000`. 🌟

## 🚀 Usage

To tap into the magic of this API, simply make HTTP GET requests to the following enchanting endpoints:

- `/api/news/crime`: Retrieve captivating news articles in the "crime" category.
- `/api/news/sport`: Discover thrilling news articles in the "sport" category.

   Example incantation:

   ```bash
   curl http://localhost:5000/api/news/crime
   ```

   Watch as the API responds with mystical JSON data containing mesmerizing news articles. 🪄✨

### Custom Response for Specific Count

Should you desire a specific number of news articles, just whisper the `count` parameter in the URL. For instance:

- `/api/news/crime/5`: Uncover the top 5 news articles in the "crime" category.

   Example conjuration:

   ```bash
   curl http://localhost:5000/api/news/crime/5
   ```

   The API shall conjure JSON data containing the exact number of news articles you seek. And should you attempt an invalid count (greater than the available news articles), fear not! The API will gently respond with an error message, accompanied by a status code of 400 (Bad Request). 🧙‍♂️🌠

## 🌐 API Endpoints

- `/api/news/crime`: Get crime news articles.
- `/api/news/sport`: Get sport news articles.
- `/api/news`: Retrieve general news articles.



## 🤝 Contributing

Join us in this enchanting journey! If you'd like to contribute your wizardry to this project, follow these mystical steps:

1. Fork the repository.
2. Create a new branch for your magical feature: `git checkout -b feature-name`
3. Cast your spells and make your changes, then commit them with a magic incantation: `git commit -m 'Add new feature'`
4. Share your wizardry by pushing to your forked repository: `git push origin feature-name`
5. Finally, send a magical scroll by creating a pull request to the main repository.

## 📜 License

This project is enchanted under the [MIT License](LICENSE). Feel free to spread the magic! 🪄📚

# :handshake: Our Contributors
<a href="https://github.com/ratnesh-maurya/News_Api_backend/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ratnesh-maurya/News_Api_backend" />
</a>
