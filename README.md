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
