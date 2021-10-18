from math import e
import speech_recognition as sr
import pyttsx3 as pt
import pywhatkit as pw
import datetime
import wikipedia
import pyjokes

engine = pt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say("Hi how can i help you")
engine.runAndWait()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def runJohn(command):
    if 'play' in command:
        command = command.replace('play', '')
        speak('playing'+command)
        pw.playonyt(command)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        speak('the time is '+time)
    
    elif 'Wikipedia' in command:
        command = command.replace('wiki', '')
        info = wikipedia.summary(command, 2)
        print(info)
        speak(info)

    elif 'what' in command:
        info = wikipedia.summary(command, 2)
        print(info)
        speak(info)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)
    

listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("Listening")
        voice = listener.listen(source, timeout=5, phrase_time_limit=5)
        command = listener.recognize_google(voice)
        print(command)
        
        # command = command.replace('John', '')
        runJohn(command)
except:
    pass

