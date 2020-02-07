from gtts import gTTS
import speech_recognition as sr
import playsound, bs4, webbrowser, requests, sys, warnings, datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

warnings.filterwarnings('ignore')    

def assistant_response(text):
    print(text)
    res = gTTS(text = text, lang="en-us", slow=False )
    res.save("assistantresponse.mp3")
    playsound.playsound('assistantresponse.mp3')
def date_now():
    now = datetime.datetime.now()
    year = now.year
    month = now.strftime("%B")
    dt = now.strftime("%d")
    day = now.strftime("%A")
    date = str(day) +" " + str(dt)+" of " + str(month)+" " + str(year)
    return date
    
def time_now():
    now = datetime.datetime.now()
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    seconds = now.strftime("%S")
    p = now.strftime("%p")
    time = str(hour) +':' + str(minute) + str(p)
    return time


def lucy_logic():
    date_q = ["what is today date","what's today's date","what is date", "which day we are in","which day is today"]
    time_q = ["what is the time now","what's time","what is the time"]
    i = 0
    while True:
        warnings.filterwarnings('ignore')
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try :
            data = r.recognize_google(audio)
            data = data.lower()
            print(str(data))
        except sr.UnknownValueError:
            i +=1
            if i>=3:
                break
            continue
        except sr.RequestError as e:
            print ("Requst error as "+ e)

        try: 
            if str(data) in date_q:
                text = date_now()
                assistant_response(text)
                i = 0
                continue
            elif str(data) in time_q :
                text = time_now()
                assistant_response(text)
                i = 0
                continue
            elif "exit" in data:
                break  
            else:
                text = "here are the results i have found"
                assistant_response(text)
                url = "https://www.google.com/search?q="+ data
                webbrowser.get().open(url)
                i = 0
                continue
        except:
            continue


def welcome ():
    waking_words = ["hey lucy","ok lucy","hello lucy"]
    while True:
        warnings.filterwarnings('ignore')
        t = sr.Recognizer()
        with sr.Microphone() as source:
            t.adjust_for_ambient_noise(source)
            aud = t.listen(source)
            try:
                tex =t.recognize_google(aud)
                tex = tex.lower()
                if str(tex)in waking_words:
                    print(tex)
                    text = "hello! what can I do for you?"
                    assistant_response(text)
                    print("listening.....")
                    lucy_logic()
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                pass
                
welcome()

        


         