# Text to Speech Converter

A simple GUI application that converts text to speech and allows you to save the output as WAV files.

## Features

- Text input with a scrollable text area
- Multiple voice selection
- Adjustable speech rate
- Save output as WAV files
- Preview speech before saving

## Requirements

- Python 3.6 or higher
- pyttsx3 library

[![text2speech.gif](https://i.postimg.cc/FFBkpTP9/text2speech.gif)](https://postimg.cc/Lhjs63K7)

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python text_to_speech_app.py
   ```
2. Enter your text in the text area
3. Select a voice from the dropdown menu
4. Adjust the speech rate using the slider
5. Click "Speak" to preview the speech
6. Click "Save as WAV" to save the audio to a file

## Notes

- The available voices depend on your system's installed text-to-speech voices
- The speech rate can be adjusted from 50 to 300 words per minute
- WAV files are saved with a timestamp in the filename by default 
