# News Reading Programme From NEWSAPI
import pywin32_system32
import win32com.client
import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speaker=Dispatch("SAPI.SpVoice")
    speaker.Speak(str)

if __name__ == '__main__':
        speak("Good Morning!!  Top Headlines is....")
        # r=requests.get("https://docs.python.org/3/library/pickle.html")
        r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=c465f7fbde114936bc54e6db79ce4786")
        b=r.text
        rstr_json=r.json()
        json_format=json.dumps(rstr_json)
        json_format_parsed_dict=json.loads(json_format)
        print(json_format_parsed_dict)
        for i in json_format_parsed_dict['articles']:
            print(i['title'])
            speak(i['title'])
        #     speak("Next Headline is")
        # speak("Thank you for Listening...")

