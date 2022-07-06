from datetime import datetime
from http import server
from re import A
from time import thread_time, thread_time_ns
from unicodedata import name
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from pygame import mixer
import smtplib



engine= pyttsx3.init()
voiceid="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
# print(voices[1].id)
engine.setProperty('voice',voiceid)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning user Sir')
    elif hour>12 and hour<=18:
        speak('Good Afternoon user sir')
    else :
        speak('Good evening user Sir')

    speak('I am Jarvis, Please tell me how may I help you ')

def takeCommand():  # it takes microphone input form the user and returns string ouput
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Jarvis Listening....')
        r.pause_threshold=1 # seconds of non-speaking audio before a phrase is considered complete
        r.adjust_for_ambient_noise(source,duration=1)
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said :{query}\n')
    except Exception as e:
        print(e)
        print('say that again please .....')
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sending email address','password') # add your email and password here
    server.sendmail('same email address',to,content) # add in this section the email address which you write above
    server.close()

if __name__ == "__main__":
      wishMe()
      while True :
        query= takeCommand().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('Searching wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=3)
            speak('According to wikipedia....')
            print(results)
            speak(results)
            speak('Thank you')
            break

        elif 'open youtube' in query :
            webbrowser.open('youtube.com')
            speak('Youtube has been opened')
            speak('Thank you so much sir')
            break
        
        elif 'open google' in query :
            webbrowser.open('google.com')
            speak('google has been opened')
            speak('Thank you')

            break
        
        elif 'open stackoverflow' in query :
            webbrowser.open('stackoverflow.com')
            speak('stackoverflow has been opened')
            speak('Thank you')
            break

        elif 'play music' in query :
            mixer.init()
            mixer.music.load('D:/PYTHONWORKSPACE/Project 2/Tola-Tola-Amitraj-Bela-Shende.mp3')
            mixer.music.play() 
            print('playing music....')
            stop=int(input('Enter number 5 to stop song\n'))
            if stop==5:
                break
            
            
            
        
            
        elif 'the time' in query:
            strTime=datetime.now().strftime("%H Hours %M minutes and %S seconds")
            print(strTime)
            speak(f" Sir The time is :{strTime}")
            speak('Thank you')
            break
        
        elif 'open visual studio code' in query:
            codepath="C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            speak('visual studio code has been opened')
            speak('Thank you')
            break

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
            speak('facebook has been opened')
            speak('Thank you')
            break

        elif 'open whatsapp' in query:
            webbrowser.open('whatsapp.com')
            speak('whatsapp has been opened')
            speak('Thank you')
            break

        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
            speak('instagram has been opened')
            speak('Thank you')
            break

        elif 'open twitter' in query:
            webbrowser.open('twitter.com')
            speak('twitter has been opened')
            speak('Thank you')
            break

        elif 'email to user' in query:
            try:
                speak('What should I say in email?')
                to='email address' # here write your email address from which you want to send an email
                content=takeCommand()
                sendEmail(to,content)
                speak('Email has been sent')
                speak('Thank you')
                break
            except Exception as e:
                print(e)
                speak('Sorry sir I am not able to send the email at this time')
                break

             