from __future__ import annotations

import argparse
import datetime as dt
import sys
import webbrowser

import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia


EXIT_COMMANDS = {"exit", "quit", "stop", "goodbye", "bye"}


class Speaker:
    def __init__(self, voice_index: int = 0, rate: int = 175) -> None:
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty("voices")
        if voices:
            voice_index = max(0, min(voice_index, len(voices) - 1))
            self.engine.setProperty("voice", voices[voice_index].id)
        self.engine.setProperty("rate", rate)

    def say(self, text: str) -> None:
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()


def normalize_command(command: str, wake_word: str = "jarvis") -> str:
    command = command.strip().lower()
    if command.startswith(wake_word.lower()):
        command = command[len(wake_word):].strip(" ,")
    return command


def listen(recognizer: sr.Recognizer, timeout: float = 5.0) -> str | None:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=8)
        return recognizer.recognize_google(audio)
    except sr.WaitTimeoutError:
        print("No speech detected.")
    except sr.UnknownValueError:
        print("I could not understand the audio.")
    except sr.RequestError as exc:
        print(f"Speech recognition service error: {exc}")
    except OSError as exc:
        print(f"Microphone error: {exc}")
    return None


def execute(command: str, speaker: Speaker) -> bool:
    """Execute one command. Return False when the assistant should stop."""
    command = normalize_command(command)

    if not command:
        return True

    if command in EXIT_COMMANDS:
        speaker.say("Goodbye.")
        return False

    if command.startswith("play "):
        song = command.removeprefix("play ").strip()
        if song:
            speaker.say(f"Playing {song}")
            pywhatkit.playonyt(song)
        return True

    if "time" in command:
        current_time = dt.datetime.now().strftime("%I:%M %p")
        speaker.say(f"The current time is {current_time}.")
        return True

    if "date" in command or "today" in command:
        current_date = dt.datetime.now().strftime("%A, %d %B %Y")
        speaker.say(f"Today is {current_date}.")
        return True

    if command.startswith("who is ") or command.startswith("what is "):
        topic = command.split(" ", 2)[2].strip()
        if not topic:
            speaker.say("Please tell me what you want to know.")
            return True
        try:
            summary = wikipedia.summary(topic, sentences=2, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as exc:
            options = ", ".join(exc.options[:5])
            summary = f"That topic is ambiguous. Some options are {options}."
        except wikipedia.exceptions.PageError:
            summary = "I could not find a matching Wikipedia page."
        except Exception as exc:
            summary = f"Wikipedia lookup failed: {exc}"
        speaker.say(summary)
        return True

    if "joke" in command:
        speaker.say(pyjokes.get_joke())
        return True

    if command in {"how are you", "how are you doing"}:
        speaker.say("I am running well. Thanks for asking.")
        return True

    if command.startswith("open "):
        site = command.removeprefix("open ").strip()
        known_sites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "github": "https://github.com",
        }
        if site in known_sites:
            speaker.say(f"Opening {site}.")
            webbrowser.open(known_sites[site])
        else:
            speaker.say("I currently support opening YouTube, Google, or GitHub.")
        return True

    if command in {"help", "commands"}:
        speaker.say(
            "Try commands like play a song, time, date, who is Ada Lovelace, "
            "tell me a joke, open YouTube, or exit."
        )
        return True

    speaker.say("I did not understand that command. Say help to hear some examples.")
    return True


def run_text_mode(speaker: Speaker) -> None:
    print("Text mode. Type 'help' for commands and 'exit' to stop.")
    while True:
        try:
            command = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not execute(command, speaker):
            break


def run_voice_mode(speaker: Speaker) -> None:
    recognizer = sr.Recognizer()
    speaker.say("Jarvis is ready.")
    while True:
        command = listen(recognizer)
        if command is None:
            continue
        print(f"You: {command}")
        if not execute(command, speaker):
            break


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Jarvis Python Voice Assistant")
    parser.add_argument(
        "--mode",
        choices=("text", "voice"),
        default="text",
        help="Use text input or microphone input. Default: text.",
    )
    parser.add_argument("--voice-index", type=int, default=0)
    parser.add_argument("--rate", type=int, default=175)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        speaker = Speaker(args.voice_index, args.rate)
    except Exception as exc:
        print(f"Text-to-speech initialization failed: {exc}", file=sys.stderr)
        return 1

    if args.mode == "voice":
        run_voice_mode(speaker)
    else:
        run_text_mode(speaker)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
