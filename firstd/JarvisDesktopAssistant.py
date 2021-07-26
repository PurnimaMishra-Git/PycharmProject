import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio

# Email writing part isnext enhnacement

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# engine.setProperty('rate',145)

def speak(aud):
    engine.say(aud)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("Good Mornning!!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!!")
    else:
        speak("Good Night!!")

    speak("I am Anna Madam How may i help you today!!!")

# It takes microphone input from the users and returns string output
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)
        print("*********************")

    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print("user said:", query)


    except Exception:
        print("Say that again please")
        return "none"

    return query





if __name__ == '__main__':
    wishme()
    while True:
        query=takecommand().lower()
#     logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("searching.....wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("accoding to wikipedia")
            speak(result)

        elif 'you tube' in query:
            speak("opening you tube....")
            webbrowser.open("youtube.com")

        elif 'open google'in query:
            webbrowser.open("google.com")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='D:\\Music'
            songs=os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir,songs[0]))# you can use random module to play randomsond by replcaing 0 with random
            speak(songs)

        elif'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f" the time is {strTime}")

