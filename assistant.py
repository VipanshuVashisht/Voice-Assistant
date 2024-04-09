import pyttsx3,datetime,wikipedia,webbrowser,os,smtplib
import speech_recognition as sr
from PyDictionary import PyDictionary
from ttkthemes import themed_tk
import tkinter as tk
from tkinter import scrolledtext
from PIL import ImageTk,Image
from functools import partial
import urllib.request,bs4 as bs,sys,threading
from tkinter import scrolledtext
import sys,wolframalpha,calendar,webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        message = "Good Morning!"
    elif hour >= 12 and hour < 18:
        message = "Good Afternoon!"
    else:
        message = "Good Evening!"
    message += " I am your personal assistant. Please tell me how may I help you\n"
    speak(message)
    add_output(message)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        message="Listening..."
        add_output(message)
        r.pause_threshold = 1
        r.energy_threshold = 10000
        audio = r.listen(source)

    try:
        print("Recognizing...")
        message="Recognizing..."
        add_output(message)
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        message=(f"User said: {query}\n")
        add_output(message)

    except Exception as e:
        print("Say that again please...")
        message="Say that again please..."
        add_output(message)
        return "None"
    return query

def news():
    webbrowser.open('https://news.google.com/')

def search(query):
    webbrowser.open(f'https://www.google.com/search?q={query}')

def screenshot():
    import pyautogui
    img = pyautogui.screenshot()
    img.save("screenshot.png")
    os.startfile("screenshot.png")

def define_word():
    dictionary=PyDictionary()

    speak("What word would you like to define?")
    word = takeCommand()

    definition = dictionary.meaning(word)

    if definition:
        speak(f"Here is the definition of {word}:")
        message=(f"Here is the definition of {word}:")
        add_output(message)
        for key in definition:
            speak(f"{key}: {definition[key][0]}")
            message=(f"{key}: {definition[key][0]}")
            add_output(message)
    else:
        speak("Sorry, I could not find a definition for that word.")


def set_reminder():
    speak("What should I remind you about?")
    reminder_text = takeCommand()

    speak("When should I remind you? Please provide the time.")
    time_str = takeCommand()

    try:
        reminder_time = datetime.datetime.strptime(time_str, "%H:%M")
        current_time = datetime.datetime.now()

        if reminder_time > current_time:
            time_difference = (reminder_time - current_time).seconds
            timer = threading.Timer(time_difference, lambda: remind_user(reminder_text))
            timer.start()
            speak(f"Reminder set for {time_str}.")
        else:
            speak("Sorry, the provided time has already passed. Please provide a future time.")
    except ValueError:
        speak("Sorry, I couldn't understand the time. Please provide the time in the format HH:MM.")

def remind_user(reminder_text):
    speak(f"Reminder: {reminder_text}")


def gen(n):
    for i in range(n):
        yield i

class MainframeThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        mainframe()

def Launching_thread():
    Thread_ID=gen(1000)
    global MainframeThread_object
    MainframeThread_object=MainframeThread(Thread_ID.__next__(),"Mainframe")
    MainframeThread_object.start()

try:
    app=wolframalpha.Client("JPK4EE-L7KR3XWP9A")
except Exception as e:
    pass

class RedirectText:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, str):
        self.text_widget.insert(tk.END, str)

def add_output(output):
    scrollable_text.config(state='normal')
    scrollable_text.insert(tk.END, output + '\n')
    scrollable_text.config(state='disabled')
    scrollable_text.see(tk.END)
    root.update()


def mainframe():
    wishMe()
    try:
        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak("Searching Wikipedia...")
                message="Searching Wikipedia..."
                add_output(message)
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                message="According to Wikipedia"
                add_output(message)
                print(results)
                speak(results)
                add_output(results)

            elif any(phrase in query for phrase in ['who is', 'who is this']):
                query = query.replace("wikipedia", "")
                try:
                    results = wikipedia.summary(query, sentences=1)
                    speak("According to Wikipedia:")
                    speak(results)
                    add_output(results)
                    print(results)
                except wikipedia.exceptions.DisambiguationError as e:
                    speak("Multiple results found. Please specify your query.")
                except wikipedia.exceptions.PageError as e:
                    speak("Sorry, I couldn't find any information on that topic.")
                
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                message = f"Sir, the time is {strTime}"
                add_output(message)
            elif any(phrase in query for phrase in ['the date']):
                strDay = datetime.date.today().strftime("%B %d, %Y")
                speak(f"Today is {strDay}")
                message=(f"Today is {strDay}")
                add_output(message)
            elif any(phrase in query for phrase in ['what day it is', 'what day is today', 'which day is today', "today's day name please"]):
                speak(f"Today is {datetime.datetime.now().strftime('%A')}")
                message=(f"Today is {datetime.datetime.now().strftime('%A')}")
                add_output(message)

            elif any(phrase in query for phrase in ['show me calendar', 'display calendar']):
                calendar_text = calendar.calendar(2023)
                add_output(calendar_text)
                speak("Here is the calendar for 2021.")

            elif 'search' in query:
                query = query.replace("search", "")
                search(query)

            elif any(phrase in query for phrase in ['define', 'what is the meaning of', 'tell me about']):
                define_word()

            elif 'take a screenshot' in query:
                speak("Taking a screenshot")
                screenshot()
                speak("Screenshot has been saved")
                message = "Screenshot has been saved"
                add_output(message)

            elif 'temperature' in query:
               try:
                   res = app.query(query)
                   result = next(res.results).text
                   speak(result)
                   add_output(result)
               except:
                   print("Internet Connection Error")
            
            elif 'news' in query:
                news()
            
            elif any(phrase in query for phrase in ('what is the capital of', 'capital of', 'capital city of')):
                try:
                    res = app.query(query)
                    result = next(res.results).text
                    speak(result)
                    add_output(result)
                except :
                    print("Error fetching the result:")

            elif any(phrase in query for phrase in ["what is my exact location", "what is my location", "my current location", "show my location"]):
                url = "https://www.google.com/maps/search/Where+am+I+?/"
                webbrowser.get().open(url)
                speak("Showing your current location on Google Maps...")
                message="Showing your current location on Google Maps..."
                add_output(message)
            
            elif any(phrase in query for phrase in ['make a note', 'take note', 'take a note', 'note it down', 'make note', 'remember this as note', 'open notepad and write']):
                speak("What would you like to write down?")
                note_text = takeCommand()
                if note_text:
                    add_output(f"Note: {note_text}")
                    with open("notes.txt", "a") as file:
                        file.write(note_text + "\n")
                    speak("I have made a note of that.")
                else:
                    speak("Sorry, I didn't catch that. Could you please try again?")

            elif 'stop' in query or 'exit' in query or 'bye' in query:
                speak("Thank you for using me. Have a nice day!")
                message = "Thank you for using me. Have a nice day!"
                add_output(message)
                break

            elif 'set reminder' in query:
               set_reminder()
            
            root.update()
            
    except Exception as e:
        pass


if __name__ == "__main__":
        root=themed_tk.ThemedTk()
        root.set_theme("winnative")
        root.geometry("{}x{}+{}+{}".format(745, 360, int(root.winfo_screenwidth() / 2 - 745 / 2),int(root.winfo_screenheight() / 2 - 360 / 2)))
        root.resizable(0, 0)
        root.title("Voice Assistant")
        root.iconbitmap('Assistant.ico')
        root.configure(bg='#2c4557')
        scrollable_text = scrolledtext.ScrolledText(root, state='disabled', height=15, width=87, relief='sunken', bd=5,wrap=tk.WORD, bg='#add8e6', fg='#800000')
        scrollable_text.place(x=10, y=10)
        
        mic_img = Image.open("mic.png")
        mic_img = mic_img.resize((55, 55), resample=Image.LANCZOS)
        
        mic_img = ImageTk.PhotoImage(mic_img)
        Speak_label = tk.Label(root, text="SPEAK:", fg="#FFD700", font='"Times New Roman" 12 ', borderwidth=0, bg='#2c4557')
        Speak_label.place(x=250, y=300)
        
        Listen_Button = tk.Button(root, image=mic_img, borderwidth=0, activebackground='#2c4557', bg='#2c4557',command=Launching_thread)
        Listen_Button.place(x=330, y=280)
        
        root.mainloop()       