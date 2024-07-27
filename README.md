# SpeechToText.py

🚀 **Introducing My New Speech Recognition and Speech-To-Text Converter!** 🗣️🔊

This project combines speech recognition and text-to-speech capabilities, allowing you to convert spoken commands into text and receive audible feedback. The tool leverages Google Text-to-Speech for online, high-quality speech conversion and offers a choice between male and female voices.

## Features
- **Voice Selection:** Choose between male and female voices for the TTS output.
- **Speech Recognition:** Accurately captures spoken commands and converts them to text.
- **Text-to-Speech Conversion:** Speaks out the recognized text using the selected voice.
- **Online Mode:** Utilizes Google Text-to-Speech for high-quality and accurate speech conversion.
- **Real-Time Interaction:** Continuously listens for user commands and provides immediate feedback.
- **Error Handling:** Robust handling for request errors and unrecognized speech.
- **Exit Command:** Simply say "exit" to stop the program gracefully.

## How It Works
1. **Initialize the Recognizer and TTS Engine:** Set up the speech recognition and text-to-speech engines.
2. **Voice Selection:** Prompt the user to choose the desired voice.
3. **Continuous Listening:** The program listens for commands, converts them to text, and provides audible feedback.
4. **Graceful Exit:** The user can exit the program by saying "exit".

## Requirements
- `speech_recognition`
- `pyttsx3`
- `gtts`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/chetangadhiya4939/SpeechToText.py.git
   ```
2. Install the required libraries:
   ```bash
   pip install speechrecognition pyttsx3 gtts
   ```

## Usage
Run the `convertor` function to start the speech-to-text and text-to-speech conversion:
```python
python SpeechToText.py
```

Feel free to explore the code, try it out, and contribute if you'd like!

---

I look forward to your feedback and suggestions. Let's make technology more accessible and interactive together! 💬🔉
