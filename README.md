# Voice Assistant with Tkinter GUI

## Description

This project implements a voice assistant with a graphical user interface (GUI) using Python's Tkinter library. The voice assistant can perform various tasks such as providing information from Wikipedia, searching the web, taking notes, setting reminders, showing the calendar, and more. Users can interact with the assistant by speaking into the microphone or typing queries into the GUI.

## Features

- Graphical user interface (GUI) for interacting with the voice assistant.
- Voice recognition and synthesis using the speech_recognition and pyttsx3 libraries.
- Integration with Wikipedia for fetching information.
- Web search functionality using the webbrowser module.
- Note-taking feature to record user input.
- Reminder setting capability with support for time-based reminders.
- Calendar display functionality to show the calendar for the current year.
- News browsing feature to open the latest news articles in the default web browser.

## Installation

To run the Voice Assistant with Tkinter GUI locally, follow these steps:

1. Install Python (if not already installed).
2. Clone this repository:

   ```bash
   git clone https://github.com/your-username/voice-assistant-tkinter-gui.git
   ```

3. Navigate to the project directory:

   ```bash
   cd voice-assistant-tkinter-gui
   ```

4. Install dependencies:

   ```bash
   pip install pyttsx3 speechrecognition wikipedia ttkthemes PyDictionary
   ```

5. Run the application:

   ```bash
   python main.py
   ```

## Usage

1. Launch the application by running the `main.py` script.
2. Speak into the microphone or type queries into the GUI.
3. Click the microphone icon or press the "Listen" button to start voice recognition.
4. Wait for the assistant to process your query and provide a response.

## Dependencies

- Python 3.x
- Tkinter library
- pyttsx3 library for text-to-speech synthesis
- speech_recognition library for speech recognition
- wikipedia library for fetching information from Wikipedia
- ttkthemes library for themed Tkinter widgets
- PyDictionary library for word definitions
