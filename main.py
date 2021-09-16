#import tkinter
#import googletrans
import speech_recognition as sr
#import datetime
#import time
import pyttsx3
import pywhatkit
import  datetime
import wikipedia
import pyjokes
import webbrowser
import weathercom
import json
import psutil
import os
#import eel
#from googletrans import Translator
#from threading import Thread
#import requests
#from bs4 import BeautifulSoup
#import tkinter as tk
#from tkinter import *
#from tkinter import  simpledialog, Tk
#from PIL import ImageTk, Image


#root = tk.Tk()
#canvas = tk.Canvas(root,height=750,width=470,bg="#263D43" )
#root.resizable(0,0)
#root.title("AI VOICE ASSISTANT ALEXA")
#canvas.pack()
#root.mainloop()



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voices[1].id)

hour = int(datetime.datetime.now().hour)
if 0 < hour < 12:
    print('Hello! Good Morning !')
    engine.say('Hello! Good Morning !')
    engine.runAndWait()
elif 12 <= hour <= 18:
    print('Hello! Good Afternoon!')
    engine.say('Hello! Good Afternoon!')
    engine.runAndWait()
else:
    print('Hello! Good Evening!')
    engine.say('Hello! Good Evening!')
    engine.runAndWait()


battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent
if not plugged:
    plugged = "Not Plugged In"
else:
    plugged = "Plugged In"
if percent <= 25 and plugged == 'Not Plugged In':
    print("I can see that your battery is less than 25%"
                      "I would advice you to plug in you charger")
    engine.say("I can see that your battery is less than 25%"
                      "I would advice you to plug in you charger")
    engine.runAndWait()


print('I am your Alexa')
engine.say('I am your Alexa')
print('What can I do for you?')
engine.say('What can I do for you?')
engine.runAndWait()

def take_command() -> voice:
    try:
        with sr.Microphone() as source:
            print('Listening...')
            listener.pause_threshold = 0.6
            listener.phrase_threshold = 0.290
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)

            else:
                print("Are you talking to me?")
                print("If yes, then please call out my name.")
                engine.say('Are you talking to me?')
                engine.say('If yes, then please call out my name.')
                engine.runAndWait()
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play','')
        print('playing'+ song)
        engine.say('playing'+ song)
        engine.runAndWait()
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        engine.say('Current time is '+time)
        engine.runAndWait()
    elif 'who is' in command:
        person=command.replace('who is','')
        info = wikipedia.summary(person, 1)
        print(info)
        engine.say(info)
        engine.runAndWait()
    elif 'what is' in command:
        topic=command.replace('what is','')
        info = wikipedia.summary(topic, 1)
        print(info)
        engine.say(info)
        engine.runAndWait()
    elif 'google' in command:
        command = command.replace('google','')
        url='https://google.com/search?q='+ command
        print('Here is what I found for' + command)
        engine.say('Here is what I found for' + command)
        engine.runAndWait()
        webbrowser.get().open(url)
    elif 'search' in command:
        command = command.replace('search','')
        url='https://google.com/search?q='+ command
        print('Here is what I found for' + command)
        engine.say('Here is what I found for' + command)
        engine.runAndWait()
        webbrowser.get().open(url)
    elif 'location' in command:
        print('What is the location?')
        engine.say('What is the location?')
        engine.runAndWait()
        loc = take_command()
        url='https://google.nl/maps/place/' + loc + '/&amp;'
        print('Here is what I found for the location' + loc)
        engine.say('Here is what I found for the location' + loc)
        engine.runAndWait()
        webbrowser.get().open(url)
    elif 'weather' in command:
        print('What is the location?')
        engine.say('What is the location?')
        engine.runAndWait()
        city = take_command()
        weatherDetails = weathercom.getCityWeatherDetails(city)
        humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
        temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
        phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
        print('Currently in ' + city + ' temperature is ' + str(temp)+ ' degree celcius. Humidity is '+ str(humidity) + ' percent. And sky is '+ phrase)
        engine.say('currently in ' + city + ' temperature is ' + str(temp)+ ' degree celcius. Humidity is '+ str(humidity) + ' percent. And sky is '+ phrase + '.')
        engine.runAndWait()

    elif 'are you single' in command:
        print('Sorry! I am currently in relationship with wifi')
        engine.say('Sorry! I am currently in relationship with wifi')
        engine.runAndWait()
    elif 'you are beautiful' in command:
        print('Thanks! Thats so sweet of you. I belive that beauty lies in the eye of beholder.')
        engine.say('Thanks! Thats so sweet of you. I belive that beauty lies in the eye of beholder.')
        engine.runAndWait()
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        print(joke)
        engine.say(joke)
        engine.runAndWait()
    elif 'who are you' in command:
        print('My name is Alexa. I am your virtual assistant. You can also take me as your friend!')
        engine.say('My name is Alexa. I am your virtual assistant. You can also take me as your friend!')
        engine.runAndWait()

   # elif 'translate' in command:
        #command = command.replace('translate', '')
        #engine.say('In which language?')
        #engine.runAndWait()
        #lang = take_command()
        #engine.say(googletrans.Translator(command, lang))
        #engine.runAndWait()

    else:
        #engine.say('Please say the command again.')
        #engine.runAndWait()
        url = 'https://google.com/search?q=' + command
        print('Here is what I found for' + command)
        engine.say('Here is what I found for' + command)
        engine.runAndWait()
        webbrowser.get().open(url)
while True:
    run_alexa()

