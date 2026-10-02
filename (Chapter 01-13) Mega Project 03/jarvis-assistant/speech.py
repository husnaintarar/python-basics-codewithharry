"""
speech.py
Handles all voice input (listening/recognition) and voice output (text-to-speech)
for Jarvis. Other modules import speak() and listen_and_recognize() from here
instead of managing the recognizer/engine themselves.
"""

import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    """Speak the given text out loud using the offline TTS engine."""
    engine.say(text)
    engine.runAndWait()


def listen_and_recognize(source, timeout=None):
    """
    Listen once on the given microphone source and return the recognized
    text in lowercase. Returns an empty string if nothing was understood,
    if the speech recognition service couldn't be reached, or if no speech
    was detected before the optional timeout (in seconds) elapsed.
    """
    try:
        audio = recognizer.listen(source, timeout=timeout)
    except sr.WaitTimeoutError:
        return ""

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return ""