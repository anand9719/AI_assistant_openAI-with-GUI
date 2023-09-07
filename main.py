import time
import speech_recognition as sr
import pyttsx3
import openai
import webbrowser
import os
import socket
from requests import get
from ip2geotools.databases.noncommercial import DbIpCity
# from geopy.distance import distance
import cv2
import pywhatkit as kit
import sys
import datetime
import subprocess
import pyautogui
import requests
openai.api_key = ""

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
hour = int(datetime.datetime.now().hour)
strTime = datetime.datetime.now().strftime("%H:%M:%S")
date = datetime.date.today()

if hour>=0 and hour<12:
    print("Good morning, Sir")
    speak("good morning sir")
elif hour>=12 and hour<=17:
    print("Good afternoon, Sir")
    speak("good afternoon sir")
else:
    print("Good evening, Sir")
    speak("good evening sir")
print(f"it's {date}, {strTime}")
speak(f"it's {date}, {strTime}")
print("Please tell me how may i help you ?")
speak("please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    mic = sr.Microphone(device_index = 1)

    with mic as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        user_input = r.recognize_google(audio)
        print(user_input)
    except Exception as e:
        speak("Say that again please...")
        return "none"
    return user_input

if __name__ == "__main__":
    conversation = ""
    user_name = "Anand"
    bot_name = "Anand Assistant"
    while True:
        user_input=takeCommand().lower()
        if 'open youtube' in user_input:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in user_input:
            webbrowser.open("https://www.google.com/")

        elif 'open git hub' in user_input:
            webbrowser.open("https://github.com/anand9719")

        elif 'open linkedin' in user_input:
            webbrowser.open("https://www.linkedin.com/in/anand-agrawal-947076203/")

        elif 'open gmail' in user_input:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

        elif 'open facebook' in user_input:
            webbrowser.open("https://www.facebook.com/anand.agrawal.58910049")

        elif 'open instagram' in user_input or 'instagram profile' in user_input:
            speak("sir, Please enter the user name correctly")
            name=input("Enter username here: ")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"Sir here is the profile of user {name}")

        elif 'open whatsapp' in user_input:
            webbrowser.open("https://web.whatsapp.com/")

        elif 'open vs code' in user_input:
            codePath = "C:\\Users\\21114802820\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open notepad' in user_input:
            codePath = "C:\\Users\\21114802820\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(codePath)

        elif "close notepad" in user_input:
            speak("ok sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif 'open command prompt' in user_input:
            os.system("start cmd")
            
        elif 'open camera' in user_input:
            subprocess.run('start microsoft.windows.camera:', shell=True)

        elif 'open calculator' in user_input:
            os.system("start calc")

        elif 'play music' in user_input:
            webbrowser.open("https://music.youtube.com/")

        elif 'where i am' in user_input or 'where we are' in user_input:
            speak("Wait sir let me check")
            ipAdd = get('https://api.ipify.org').text
            print(ipAdd)
            url = f"https://get.geojs.io/v1/ip/geo/{ipAdd}"
            geo_requests = requests.get(url)
            geo_data = geo_requests.json()
            city =  geo_data['city']
            country=geo_data['country']
    
        elif 'shut down the system' in user_input:
            os.system("shutdown /s /t 5")

        elif 'restart the system' in user_input:
            os.system("shutdown /r /t 5")

        elif 'switch the window' in user_input:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif 'tell me news' in user_input:
            print("please wait sir, fetching the latest news")
            speak("please wait sir, fetching the latest news")
            main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=79688a366f7848519b7f9e22a787cb60'
            main_page = requests.get(main_url).json()
            articles = main_page["articles"]
            head = []
            day = ["first","second","third","fourth","fifht","sixth","seventh","eighth"]
            for ar in articles:
                head.append(ar["title"])
            for i in range(len(day)):
                print(f"today's {day[i]} news is: {head[i]}")
                speak(f"today's {day[i]} news is: {head[i]}")

        elif 'send message' in user_input:
            speak("sir, Please enter the phone number")
            num=input("Enter phone number here: ")
            speak("sir, Please enter your message")
            message=input("Enter your message: ")
            kit.sendwhatmsg_instantly(f"+91{num}", f"{message}")
        
        elif 'you can sleep' in user_input:
            speak("Thanks for using me sir, have a good day")
            print("Thanks for using me sir, have a good day")
            sys.exit()
        
        prompt = user_name+":"+user_input+"\n"+bot_name+":"
        conversation += prompt

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=conversation,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_str = response["choices"][0]["text"].replace("\n", "")
        response_str = response_str.split(user_name + ":",1)[0].split(bot_name + ":",1)[0]

        conversation += response_str + "\n"
        print(response_str)

        engine.say(response_str)
        engine.runAndWait()
        speak("Do you have any other work")
        print("Do you have any other work")
