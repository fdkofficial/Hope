import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import pyaudio
import pylisten
import time
import pyjokes
import requests
from bs4 import BeautifulSoup
import folium
import socket
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio=r.listen(source)
        try:
            print("Recognizing")
            query=r.recognize_google(audio)
            print("The command is printed",query)
        except Exception:
            print("Say that again sir")
            return "None"
        return query
def intro():
    print("before Continue please provide us your name ")
    speak("before Continue please provide us your name ")
def Hello():
    user=input("Enter you name : ")
    print(f'Hello! {user} I am Hope your friend how may I help you')
    speak(f'Hello! {user} I am Hope your friend how may I help you')
def getdata(url):
    req=requests.get(url)
    return r.text
    myurl="http://covid-19tracker.milkeninstitute.org/"
    htmldata=getdata(myurl)
    soup=BeautifulSoup(htmldata,'html.parser')
    myclass="is_h5-2 is_developer w-richtext"
    result=str(soup.find_all("div",class_=myclass))
    print("No 1 - "+ result[46:86])
    print("No 1 - "+ result[139:226])
    print("No 1 - "+ result[279:305])
    print("No 1 - "+ result[428:437])
def speak(audio):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(audio)
    engine.runAndWait()
def tellTime():
    time=str(datetime.datetime.now())
    dayy=datetime.datetime.now()
    print(dayy.strftime("%A"))
    print(time)
def weather1():
    CITY=input("enter city name : ")
    API_KEY= "38baeb21b5625cb8ae242a419cc24fb0"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    URL = BASE_URL +"appid="+ API_KEY +"&q="+ CITY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        print(f"{CITY:-^30}")
        print(f"Temperature: {temperature}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {report[0]['description']}")
        speak(f"{CITY:-^30}")
        speak(f"Temperature: {temperature}")
        speak(f"Humidity: {humidity}")
        speak(f"Pressure: {pressure}")
        speak(f"Weather Report: {report[0]['description']}")
    else:
        print("Error in the HTTP request")
def mapp():
    m=folium.Map(location=[45.5236,-122.6750])
    m.save('index.html')
def ipad():
    hn=socket.gethostname()
    ipadd=socket.gethostbyname(hn)
    print("My Ip is : "+ipadd)
    speak("My Ip is : "+ipadd)
def TakeQuery():
    intro()
    Hello()
    while True:
        query=takeCommand().lower()
        if 'open java' in query:
            speak('Opening Javatpoint')
            webbrowser.open("www.javatpoint.com")
        elif 'tell me a joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
        elif 'open map' in query:
            mapp()
        elif 'what is the weather' or 'weather' in query:
            weather1()
        elif 'open google' in query:
            speak('Opening Google')
            webbrowser.open("www.google.com")
        elif 'from wikipedia' in query:
            speak("Checking the Wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=6)
            speak("According to wikipedia")
            speak(result)
        elif 'tell me about you' in query:
            print("Iam Hope your Virtual Assistant created by Team V")
            print("Team V is a group with members like Fardeen khan Mukkaiyara Simran and Taj")
            speak("Iam Hope your Virtual Assistant created by Team V")
            speak("Team V is a group with members like Fardeen khan Mukkaiyara Simran and Taj")
        elif 'tell me the day' in query:
            tellTime()
        elif 'search' in query:
            query=query.replace("search","")
            webbrowser.open("www.google.com/search?q="+query)
        elif 'my ip address' in query:
            print("here")
            ipad()
        elif 'open instagram' in query:
            speak("Opening Instagram")
            webbrowser.open("www.Instagram.com/fdkofficial")
        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open("www.Youtube.com")
        elif 'open facebook' in query:
            speak("Opening facebook")
            webbrowser.open("www.fb.com")
        elif 'covid-19' in query:
            def getdata(url):
                req=requests.get(url)
                return req.text
            myurl="http://covid-19tracker.milkeninstitute.org/"
            htmldata=getdata(myurl)
            soup=BeautifulSoup(htmldata,'html.parser')
            myclass="is_h5-2 is_developer w-richtext"
            result=str(soup.find_all("div",class_=myclass))
            print("No 1 - "+ result[46:86])
            print("No 2 - "+ result[139:226])
            print("No 3 - "+ result[279:305])
            print("No 4 - "+ result[428:437])
            speak("No 1 - "+ result[46:86])
            speak("No 2 - "+ result[139:226])
            speak("No 3 - "+ result[279:305])
            speak("No 4 - "+ result[428:437])
        elif 'open translator' in query:
            from googletrans import Translator
            text=input("enter here : ")
            translator=Translator()
            dt=translator.detect(text)
            print(text)
            translate=translator.translate(text)
            print(translate.text)
        elif 'open bot' in query:
            speak("Welcome "*4)
            print("Welcome "*4)
            time.sleep(2.0)
            speak("Hello Im G one an AI Bot Created by The Great Fardeen Khan")
            time.sleep(2.0)
            print("How can I help you ?")
            time.sleep(1.0)
            print('''Type 1 for Sign Up
Type 2 for Log in''')
            opt1=int(input("Enter the Value : "))
            if opt1==1:
                name=input("Enter you Name : ")
                password=input("Enter Password : ")
                mail=input("Enter Gmail address : ")
                user=input("Enter Username : ")
                print(f'hey,,{name} You are now a part of our group')
            if opt1==2:
                name=input("Enter you UserName : ")
                password=input("Enter Password : ")
                print(f'Welcome Back {name}')
                speak(f'Welcome Back {name}')
            else:
                print("Invalid ")
            def G_one():
                time.sleep(2.0)
                print("What can I do for You ?")
                print('''
Type 1 for ChitChat
Type 2 for CalcBot
Type 3 for money converter
Type 4 To Log Out ''')
                opt2=int(input("Enter The Value " ))
                if opt2==1:
                    name1=input("What is your name ?: ")
                    time.sleep(1.0)
                    print(f'Nice name {name1} Im G.one')
                    speak(f'Nice name {name1} Im G.one')
                    fav1=input("Who is your favourite Actor ?: ")
                    time.sleep(1.0)
                    print("Nice,, I love Srk,Sidharth and Shraddha ")
                    speak("Nice,, I love Srk,Sidharth and Shraddha ")
                    fav2=input("Which is your favourite series ?: ")
                    print(f'ohh {fav2} mine is The Originals')
                    speak(f'ohh {fav2} mine is The Originals')
                    time.sleep(1.0)
                    print("Okk so now I have to go, Im not berozgaar like you ")
                    def prev():
                        G_one()
                    prev()
                if opt2==2:
                    print("What do you want ? : ")
                    time.sleep(1.0)
                    print(''' 1)Addition
2)SUbtraction
3)Division
4)Multiplication''')
                    choice=int(input("Enter The Value " ))
                    num1=int(input("Enter no. : "))
                    num2=int(input("Enter no. : "))
                    if choice==1:
                        add=num1+num2
                        print(add)
                        def prev1():
                            G_one()
                        prev1()
                    if choice==2:
                        sub=num1-num2
                        print(sub)
                        def prev2():
                            G_one()
                        prev2()
                    if choice==3:
                        dev=num1/num2
                        print(dev)
                        def prev3():
                            G_one()
                        prev3()
                    if choice==4:
                        mul=num1*num2
                        print(mul)
                        def prev4():
                            G_one()
                        prev4()
                if opt2==3:
                    a=int(input("Enter the ammount : "))
                    print("What do you want " )
                    print("1) Dollar to Rs  2) Rs to Dollar ")
                    b=int(input("Enter what you want "))
                    if b==1:
                        c=a*75
                        print(c)
                        def prev5():
                            G_one()
                        prev5()
                    else:
                        c=a/75
                        print(c)
                        def prev6():
                            G_one()
                        prev6()
                if opt2==4:
                    print("Good bye")
            G_one()
        elif 'bye' in query:
            print("Bye")
            speak("bye")
            break
            
if __name__ == '__main__':
    TakeQuery()
