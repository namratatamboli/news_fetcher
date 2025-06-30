# News Fetcher 🗞️

A minimal Python script that fetches the latest news articles and their links using the NewsAPI, based on your search query.

## Features

- Takes user input for a search topic
- Fetches real-time news articles sorted by latest published date
- Displays article titles with clickable URLs
- Uses `.env` file to securely manage API keys

## Setup Instructions

1. Install dependencies:
```bash
pip install requests python-dotenv
```

2. Create a `.env` file in the project directory and add your NewsAPI key:
```
NEWS_API_KEY=your_api_key_here
```

3. Run the script:
```bash
python main.py
```

## Example

```
📰 What kind of news would you like to read today?: space

1) Title : NASA to Launch New Telescope
   🔗 url : https://example.com/article1

2) Title : SpaceX Mission Success
   🔗 url : https://example.com/article2

...
```

> 💡 To open links, hold `Ctrl` and click on the URL in supported terminals.

## File Structure

```bash
news_fetcher/
├── main.py
├── .env.example
├── .gitignore
└── README.md
```

## Notes

- Uses `requests` to make API calls
- Parses JSON response to extract and print news articles

## Author  
Namrata Tamboli
