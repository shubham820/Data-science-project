import datetime
import os
import smtplib
import webbrowser
import pyttsx3
import speech_recognition as sr
import wikipedia as wikipedia
import json

engine = pyttsx3.init('sapi5')
# microsoft sound api
voices = engine.getProperty('voices')

engine.setProperty('voic',voices[1].id)

with open(r"C:\Users\shubham\PycharmProjects\web\socialmedia\Home\config.json",'r') as auther:
    params = json.load(auther)["host_email"]

def speak(audio):
    ''' in this jarvis will be able to speak '''
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    speak("i would like to ask your name")
    name = takeCommand()
    autherName = str(name)
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak('Good Morning')
    elif hour>=12 and hour< 18 :
        speak('good Afternoon')
    else:
        speak('Good evening')
    if autherName == "None":
        speak(f" how are you buddy  I am a jaarvis. shubham create me to help you . so tell me how may i help you")
    else:
        speak(f" how are you {autherName} I am a jaarvis. shubham create me to help you . so tell me how may i help you")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)

        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
        print(audio)
    try:
        print("Recognizing...")
        command = r.recognize_google(audio ,language='en-in')  # Using google for voice recognition.
        print(f"User said: {command}\n")  # User command will be printed.

    except Exception as e:
        # print(e)
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return command

def sendEmail(reciever_email,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(params["email"],params["password"])
    server.sendmail(params["email"],reciever_email,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        # logic to perform task
        command =  takeCommand().lower()
        numerical = range(0,10)       
        if 'wikipedia' in command:
            speak(' searching wikipedia...')
            command = command.replace('wikipedia','')
            results = wikipedia.summary(command, sentences=2 )
            speak("according to wikipedia")
            speak(results)
        elif 'open youtube' in command:
            speak('opening youtube ....')
            webbrowser.open("http://www.youtube.com")
        elif 'open google' in command:
            speak('opening google...')
            webbrowser.open("http://www.google.com")
        elif 'stack overflow' in command:
            speak('opening stackoverflow...')
            webbrowser.open("http://www.stackoverflow.com")
        elif 'play music' in command:
            music_dir =(r"C:\Users\shubham\Music")
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'time' in command:
            speak(str(datetime.datetime.now()))
        elif 'pycharm' in command:
            pycham = (r"C:\Users\shubham\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            os.startfile(pycham)
        elif 'open browser' in command:
            browser = (r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
            os.startfile(browser)

        # sending the email
        elif 'send email' in command or 'email' in command :
            try:
                speak("tell me the email")
                person_email1 = takeCommand()
                person_email = str(person_email1)
                if person_email == "None":
                    speak("you do not say anything")
                else:
                    take_email_final1 = ""
                    for i in person_email:
                        if i == " ":
                            pass
                        else:
                            take_email_final1 = take_email_final1+i.lower()
                    
                    take_email_final = take_email_final1
                    print(take_email_final)
                    reciever_email = (f"{take_email_final}@gmail.com")
                    verf = speak(f"you said: {take_email_final}@gmail.com")
                    reciever_email = (f"{take_email_final}@gmail.com")
                    speak("what would you like to send in this email")
                    content = takeCommand()
                    sendEmail(reciever_email,content)
                    speak("the email has been sent")
            except Exception as e:
                speak("sorry i am not able to send this email")
        elif 'vcs' in command:
            webbrowser.open("http://www.github.com")
