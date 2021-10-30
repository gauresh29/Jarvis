import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hours = int(datetime.datetime.now().hour)
    #print(hours)
    if hours >= 0 and hours < 12:
        speak("Good morning ")
    elif hours >= 12 and hours < 16:
        speak("Good afternoon ")
    elif hours >= 16 and hours < 19:
        speak("Good evining ")
    else:
        speak("Good Night ")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    # speak("gauresh is good boy")
    wishme()
    # question = input("What is your question? ")
    # print(wikipedia.summary(question))
    while True:
    #if 1:
        query = takeCommand().lower()
        #logic for executing task based on queryif 'wikipedia' in query:

        if 'wikipedia' in query:
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'google' in query:
            
            webbrowser.open("google.com")
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            my_dir = "D:\\Jarvis\\so"
            songs= os.listdir(my_dir)
            print(songs)
            
            mysongnum= len(songs)
            print(mysongnum)
            suprisenum=random.randint(0,mysongnum)
            print(suprisenum)
            os.startfile(os.path.join(my_dir,songs[suprisenum]))
        
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,time is {strtime}")

        elif 'open code' in query:
            filepath = "C:\\Users\\gmshi\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(filepath)