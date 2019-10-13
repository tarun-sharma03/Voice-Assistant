# This program upon execution will take your command to play music randomly.
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install SpeechRecognition
import os
import datetime
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id) #voices[0].id for male assistant

#speak function to speak the string passed to it.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#function to listen your command and process them
def takedata():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')  #language set is Indian English
        print("The user said ",query)
    except Exception :
        print("Seems like i had some problem understanding that...could you please repeat it ?")
        return 'None'
    return query

#function gives the greeting message to the user.
def wishme():
    hours = datetime.datetime.now().hour

    if hours>=0 and hours <12:
        speak("good morning")
    elif hours>=12 and hours <18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("sir i am your personal assistant. tell me how can i help you ")

wishme()
query = takedata() 
if 'play music' or 'play songs' in query:
    music_dir = "F:\\Songs" #put the location of the folder where you store your songs
    songs = os.listdir(music_dir)
    l = len(songs)
    num = random.randrange(0,l,1)
    os.startfile(os.path.join(music_dir,songs[num]))
    speak("Thank you for using my sevices. All improvements on my github repository are welcome.")
    print("www.github.com/tarun-sharma03")
    exit()
else:
    speak("Query type not supported")
