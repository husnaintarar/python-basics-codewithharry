"""
commands.py
Contains all of Jarvis's "skills" — the actual actions it can take once a
command has been recognized: opening websites, playing music, fetching news,
and answering open-ended questions via Gemini.
"""

import os
import webbrowser
import requests
from dotenv import load_dotenv
from google import genai

import musicLibrary
from speech import speak

load_dotenv()

NEWS_API_KEY = os.getenv("NEWSAPI_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
gemini_client = genai.Client(api_key=GEMINI_API_KEY)

# Site name -> URL, used by open_website()
WEBSITES = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "facebook": "https://facebook.com",
    "linkedin": "https://linkedin.com",
}


def open_website(site_name):
    """Open a known website by name (e.g. 'youtube') in the default browser."""
    url = WEBSITES[site_name]
    speak(f"Opening {site_name.capitalize()}")
    webbrowser.open(url)


def play_music(song):
    """Look up a song in musicLibrary and open its link, or apologize if missing."""
    if song in musicLibrary.music:
        speak(f"Playing {song}")
        webbrowser.open(musicLibrary.music[song])
    else:
        speak(f"Sorry, I don't have {song} in your music library")


def get_news():
    """Fetch and speak the top 5 US headlines from NewsAPI."""
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["status"] != "ok":
        speak("Sorry, I couldn't fetch the news right now")
        return

    articles = data["articles"][:5]

    speak("Here are the top headlines")
    for article in articles:
        print("-", article["title"])
        speak(article["title"])


def ask_ai(question):
    """Send an open-ended question to Gemini and speak the response."""
    try:
        response = gemini_client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )
        answer = response.text
        print("AI:", answer)
        speak(answer)
    except Exception as e:
        print("AI error:", e)
        speak("Sorry, I couldn't reach the AI right now")