# Jarvis Python Voice Assistant

A cleaned and rebuilt Python desktop assistant based on the older `JArvis1.zip`, `Jarvis.zip`, and `Alexa.py` experiments from the original Python programming repository.

## Features

- text-command mode for easy testing
- microphone/voice-command mode
- text-to-speech responses
- YouTube playback
- current time and date
- Wikipedia summaries
- random jokes
- open YouTube, Google, or GitHub
- graceful `exit` / `quit` / `stop`
- recognition and microphone error handling

## What Was Fixed

The original files had several problems:

- `if __name__ == "__main_"` was misspelled
- `pyttsx3.init('sapis')` used an invalid/incorrect Windows driver name
- the larger `Jarvis.zip` mostly contained a PyCharm starter file and an entire `venv/`
- the original Alexa script could return an undefined `command`
- commands were converted to lowercase but compared against mixed-case strings
- the wake-word comparison was therefore unreliable
- a broad empty `except` hid all errors
- there was no clean exit command
- the script ran forever
- PyCharm metadata and the virtual environment were bundled with source code

The rebuilt version removes those issues and keeps dependencies in `requirements.txt`.

## Requirements

- Python 3.10+
- microphone for voice mode
- internet access for Google speech recognition, Wikipedia and YouTube commands

## Setup

```bash
git clone https://github.com/Dewannoor28/Jarvis-Python-Voice-Assistant.git
cd Jarvis-Python-Voice-Assistant

python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux/macOS:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

## Run in Text Mode

```bash
python main.py --mode text
```

Example commands:

```text
time
date
who is Ada Lovelace
play Imagine Dragons Believer
tell me a joke
open youtube
help
exit
```

## Run in Voice Mode

```bash
python main.py --mode voice
```

If microphone support fails on Windows, verify that Python can access your microphone and that PyAudio installed correctly.

## Project Structure

```text
Jarvis-Python-Voice-Assistant/
├── main.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Privacy

Voice mode uses the `SpeechRecognition` Google recognizer, so audio recognition requires an online service. Do not use it for sensitive speech unless you are comfortable with the service being used.

## Author

**Dewan Nafiul islam Noor**

GitHub: `https://github.com/Dewannoor28`
