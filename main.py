from deepface import DeepFace
import cv2
import face_recognition
import time
from pyttsx3 import engine
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes


def hear():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = listener.listen(source, timeout=5, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            
    except:
        pass
    
    return command

def speak(text):
    engine.say(text)
    engine.runAndWait()

def RunJohn(state):
    if state == 'happy':
        text = "Hey You are looking so happy, what is the reason"
        speak(text)
    
    elif state == 'sad':
        text = "Hey you look so sad, what happend. i am also so sad since you are sad. OK let me tell you joke"
        speak(text)
        speak(pyjokes.get_joke())
        speak("How do you feel now")
        ans = hear()
        if ans == 'Yes':
            speak('Hurray I am also happy')
        else:
            speak("OK I will play a motivational video for you")
            RunJohn("motivation")
    
    elif state == "motivation":
        speak("playing motivational video on youtube")
        pywhatkit.playonyt("motivational video in english")

    elif state == "neutral":
        speak("You seem so neutral, lets listen to some music, tell the song name")
        song = hear()
        speak("playing"+song)
        pywhatkit.playonyt(song)

    elif state == "surprise":
        speak("why are you so surprised, hahaha")

    else:
        speak("Your in "+state+"state")
 

engine = pyttsx3.init()
cap = cv2.VideoCapture(0)
i = 0
while (i < 5):
    isTrue, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    i += 1
    predictions = DeepFace.analyze(img)
cap.release()
cv2.destroyAllWindows()

state = predictions['dominant_emotion']
print(state)
RunJohn(state)

