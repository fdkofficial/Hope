from tkinter import *
root=Tk()
import os
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
import json
from bs4 import BeautifulSoup
from PIL import *
from PIL import ImageTk,Image
import socket
def frame():
    global f2
    f2=Frame()
    f2.place(x=100,y=100,height=310,width=450)
    f2.configure(background="black")
    img3=Label(f2,image=bg2)
    img3.place(x=0,y=0)
    speak("before Continue please provide us your name ")
    label1=Label(f2,text="Before Continue please provide us your name",fg="black",bg="#7CD7EA",font=("",15))
    label1.place(x=10,y=5)
    global ent
    ent=Entry(f2)
    ent.place(x=100,y=50)
    #btn2=PhotoImage(f2,file='submit1.png')
    sub=Button(f2,text="Submit",image=btn2,bd=0,bg='#C5F6FB',activebackground='#C5F6FB')
    sub.place(x=100,y=100)
    sub.configure(command=TakeQuery)
    label2=Label(f2,text="Name : ",fg="black",bg="#7CD7EA",font=("Garamond",15))
    label2.place(x=20,y=45)
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
# intro():
    #speak("before Continue please provide us your name ")
def Hello():
    global user
    user=ent.get()
    #user=input("Enter you name : ")
    print(f'Hello! {user} I am Hope your friend how may I help you')
    speak(f'Hello! {user} I am Hope your friend how may I help you')
def getdata(url):
    req=requests.get(url)
    return req.text
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
def ipad():
    hn=socket.gethostname()
    ipadd=socket.gethostbyname(hn)
    print("My Ip is : "+ipadd)
    speak("My Ip is : "+ipadd)
def calc():
    root1=Frame()
    root1.configure(background="black",height=380,width=380)
    #root1.geometry("380x380")
    root1.place(x=0,y=0)
    global img1
    img1=ImageTk.PhotoImage(file="bgg.png")
    lab=Label(root1,image=img1)
    lab.place(x=0,y=0)
    a=StringVar()
    b=StringVar()
    def Calculator1():
        def show(c):
            a.set(a.get()+c)
        def eq():
            global inv
            try:
                ex=a.get()
                a.set(eval(ex))
            except Exception:
                inv=Label(root1,text="Invalid input")
                inv.place(x=10,y=2)
        def clear():
            try:
                cl=a.get()
                a.set("")
                inv.destroy()
            except Exception:
                print("done")
        l1=Entry(root1,justify="right",font=("Cooper black",30),bg="black",fg="white",textvariable=a)
        l1.place(x=0,y=0,height="60",width="380")
        b1=Button(root1,text="7",font=("Cooper black",15),bd=3)
        b1.place(x=5,y=70,height="55",width="50")
        b1.configure(command=lambda:show("7"))
        b2=Button(root1,text="8",font=("Cooper black",15),bd=3)
        b2.place(x=60,y=70,height="55",width="50")
        b2.configure(command=lambda:show("8"))
        b3=Button(root1,text="9",font=("Cooper black",15),bd=3)
        b3.place(x=115,y=70,height="55",width="50")
        b3.configure(command=lambda:show("9"))
        b4=Button(root1,text="4",font=("Cooper black",15),bd=3)
        b4.place(x=5,y=140,height="55",width="50")
        b4.configure(command=lambda:show("4"))
        b5=Button(root1,text="5",font=("Cooper black",15),bd=3)
        b5.place(x=60,y=140,height="55",width="50")
        b5.configure(command=lambda:show("5"))
        b6=Button(root1,text="6",font=("Cooper black",15),bd=3)
        b6.place(x=115,y=140,height="55",width="50")
        b6.configure(command=lambda:show("6"))
        b7=Button(root1,text="1",font=("Cooper black",15),bd=3)
        b7.place(x=5,y=210,height="55",width="50")
        b7.configure(command=lambda:show("1"))
        b8=Button(root1,text="2",font=("Cooper black",15),bd=3)
        b8.place(x=60,y=210,height="55",width="50")
        b8.configure(command=lambda:show("2"))
        b9=Button(root1,text="3",font=("Cooper black",15),bd=3)
        b9.place(x=115,y=210,height="55",width="50")
        b9.configure(command=lambda:show("3"))
        b10=Button(root1,text="+",font=("Cooper black",15),bd=3)
        b10.place(x=240,y=70,height="55",width="50")
        b10.configure(command=lambda:show("+"))
        b11=Button(root1,text="-",font=("Cooper black",15),bd=3)
        b11.place(x=300,y=70,height="55",width="50")
        b11.configure(command=lambda:show("-"))
        b12=Button(root1,text="*",font=("Cooper black",15),bd=3)
        b12.place(x=240,y=140,height="55",width="50")
        b12.configure(command=lambda:show("*"))
        b13=Button(root1,text="/",font=("Cooper black",15),bd=3)
        b13.place(x=300,y=140,height="55",width="50")
        b13.configure(command=lambda:show("/"))
        b14=Button(root1,text="C",font=("Cooper black",15),bd=3)
        b14.place(x=5,y=280,height="55",width="50")
        b14.configure(command=clear)
        b15=Button(root1,text="0",font=("Cooper black",15),bd=3)
        b15.place(x=60,y=280,height="55",width="50")
        b15.configure(command=lambda:show("0"))
        b16=Button(root1,text="=",font=("Cooper black",15),bd=3)
        b16.place(x=115,y=280,height="55",width="50")
        b16.configure(command=eq)
        b17=Button(root1,text="power",font=("Cooper black",15),bd=3)
        b17.place(x=260,y=210)
        b17.configure(command=lambda :show("**"))
    Calculator1()
    root1.mainloop()
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
def TakeQuery():
    Hello()
    while True:
        query=takeCommand().lower()
        if 'open java' in query:
            speak('Opening Javatpoint')
            webbrowser.open("www.javatpoint.com")
        elif 'open calculator' in query:
            calc()
        elif 'tell me a joke' in query:
            print(pyjokes.get_joke())
            speak(pyjokes.get_joke())
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
        elif 'open chatbot' in query:
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
            elif opt1==2:
                name=input("Enter you UserName : ")
                password=input("Enter Password : ")
                print(f'Welcome Back {name}')
                speak(f'Welcome Back {name}')
            else:
                print("invalid")
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
                elif opt2==2:
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
                    elif choice==2:
                        sub=num1-num2
                        print(sub)
                        def prev2():
                            G_one()
                        prev2()
                    elif choice==3:
                        dev=num1/num2
                        print(dev)
                        def prev3():
                            G_one()
                        prev3()
                    elif choice==4:
                        mul=num1*num2
                        print(mul)
                        def prev4():
                            G_one()
                        prev4()
                    else:
                        print("invalid")
                elif opt2==3:
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
                elif opt2==4:
                    print("Good bye")
                else:
                    print("invalid")
            G_one()
        elif 'what is the weather' in query:
            weather1()
        elif 'shutdown' in query:
            print("Bye")
            speak("bye")
            f1.destroy()
            root.destroy()
            break            
#if __name__ == '__main__':
    #TakeQuery()
root.geometry("600x420")
root.configure(background="black")
root.title("Hope : The Virtual Assistant")
root.resizable(height=0,width=0)
bg=PhotoImage(file='bg1.png')
bg2=PhotoImage(file='bg2.png')
btn1=PhotoImage(file='let.png')
btn2=PhotoImage(file='submit1.png')
btn3=PhotoImage(file='ready.png')
f1=Frame()
f1.place(x=0,y=0,height=420,width=600)
f1.configure(background="black")
img=Label(f1,image=bg)
img.place(x=0,y=0)
#lab=Label(f1,text="Hope - The Virtual Assistant",font=("Bradley","15"),bg="black",fg="white")
#lab.place(x=5,y=5)
b1=Button(f1,height=60,width=140,image=btn1,bd=0,bg='#00242D',activebackground='#00242D',command=frame)
b1.place(x=380,y=290)
root.mainloop()
