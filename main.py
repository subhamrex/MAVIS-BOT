
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from tkinter import *
import pyttsx3 as pp
import speech_recognition as s
import wikipedia
import webbrowser
#import threading
import datetime
import logging 
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL) # removing No value for search_text

engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0])

def speak(word):
    engine.say(word)
    engine.runAndWait()
# def wishMe():
#     hour = int (datetime.datetime.now().hour) 
#     if hour>=4 and hour<12:
#         speak("Good Morning!")
#     elif hour>=12 and hour<18:
#         speak("Good Afternoon!")
#     else: 
#         speak("Good Evening!")
#     speak("I am Lucy Sir, Please tell me how may i help you?")      



bot = ChatBot("MAVIS",logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation'
        ,'chatterbot.logic.TimeLogicAdapter'
   ])

conversation = [
    'hello',
    'hi there',
    'what is your name ?',
    'My name is MAVIS , i am created by Subham',
    'how are you ?',
    'I am doing great these days',
    'thank you',
    'In which city you live ?',
    'I live in Kolkata',
    'In which language you talk?',
    ' I mostly talk in english'
]

trainer = ListTrainer(bot)

trainer.train(conversation)
def take_query():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("Listening...")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio,language='eng-in')
            print(query)
            textF.delete(0,END)
            textF.insert(0,query)
            send_to_MAVIS()
        except Exception:
              print("Say that again please sir...")    

        
def send_to_MAVIS():
    query = textF.get()
    if 'wikipedia' in query:
        query = query.replace("wikipedia","")
        answer_from_MAVIS = wikipedia.summary(query,sentences=1)
    elif "open youtube" in query:
        answer_from_MAVIS= "Openning Youtube"
        webbrowser.open("youtube.com") 
    elif 'open google' in query:
        answer_from_MAVIS= "Openning Google"
        webbrowser.open("google.com") 

    elif 'open facebook' in query:
        answer_from_MAVIS= "Openning Facebook"
        webbrowser.open("facebook.com") 
        
    elif 'open twitter' in query:
        answer_from_MAVIS= "Openning Twitter"
        webbrowser.open("twitter.com")   

    elif 'open instagram' in query:
        answer_from_MAVIS= "Openning Instagram"
        webbrowser.open("instagram.com")     

    elif 'open stackoverflow' in query:
        answer_from_MAVIS= "Openning stackoverflow"
        webbrowser.open("stackoverflow.com")  

    elif 'open github' in query:
        answer_from_MAVIS= "Openning Github"
        webbrowser.open("github.com")           
                 
    else:
        answer_from_MAVIS = bot.get_response(query)
        
    msg.insert(END,"You: "+ query)
    msg.insert(END,"MAVIS: "+ str(answer_from_MAVIS))
    speak(answer_from_MAVIS)
    textF.delete(0, END)
    msg.yview(END)
    

      
main = Tk()
main.geometry("500x650")
main.title("MAVIS")
img = PhotoImage(file="myai.png")
photoL = Label(main,image = img)
photoL.pack(pady=5)
frame = Frame(main)
sc = Scrollbar(frame)
msg = Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msg.pack(side = LEFT,fill=BOTH,pady=10)
frame.pack()
#creating text fileld
textF = Entry(main,font=("Verdana",20))
textF.pack(fill = X,pady=10) 
#buttons
btn = Button(main,text = "Send",font=("Verdana",20),command=send_to_MAVIS)
btn.pack()
#creating func to enter key
def enter_func(event):
    btn.invoke()
# def turn_off_VC(event):
#     btn2.invoke()    
main.bind('<Return>',enter_func)   
#main.bind('<Return>',turn_off_VC)   

def repeatL():
    while True:
        take_query() 
t = threading.Thread(target=take_query)
t.start()
main.mainloop()
  
