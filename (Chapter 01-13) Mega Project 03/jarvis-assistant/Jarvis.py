"""
Jarvis.py
The main entry point. Runs the wake-word loop and routes recognized
commands to the appropriate function in commands.py.
"""

import speech_recognition as sr

from speech import recognizer, speak, listen_and_recognize
from commands import open_website, play_music, get_news, ask_ai, WEBSITES


def handle_command(command):
    """Decide what to do with a recognized command."""
    print("Command received:", command)

    for site_name in WEBSITES:
        if f"open {site_name}" in command:
            open_website(site_name)
            return

    if "play" in command:
        song = command.replace("play", "").strip()
        play_music(song)
        return

    if "news" in command:
        get_news()
        return

    # Fallback: anything else goes to the AI
    ask_ai(command)


def main():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.pause_threshold = 0.8

        COMMAND_TIMEOUT = 6          # seconds to wait per listen attempt
        MAX_IDLE_SECONDS = 30        # total silence before auto-shutdown

        while True:
            print("Listening for wake word...")
            text = listen_and_recognize(source)

            if "jarvis" in text:
                speak("Ya?")
                idle_seconds = 0

            while True:
                    print("Listening for command...")
                    command = listen_and_recognize(source, timeout=COMMAND_TIMEOUT)

                    if not command:
                        idle_seconds += COMMAND_TIMEOUT

                        if idle_seconds >= MAX_IDLE_SECONDS:
                            speak("No activity detected. Goodbye!")
                            return

                        continue  # keep listening, don't go back to sleep yet

                    idle_seconds = 0

                    if "goodbye" in command or "stop listening" in command:
                        speak("Goodbye!")
                        return

                    handle_command(command)

    print("Jarvis has shut down.")


if __name__ == "__main__":
    main()