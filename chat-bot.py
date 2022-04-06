from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import threading
import speech_recognition as s

import pyttsx3 as pp
bot = ChatBot('my bot')

engine=pp.init()

voice=engine.getProperty('voices')
print(voice)

engine.setProperty('voice',voice[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()
convo=['hello',
       'hi there',
       'What is your name',
       'my name is karishma',
       'in which city you live?',
       'i live i jaipur',
       'how are you',
       'im good'
       'what is your mom name',
       'kamlesh',
       'who is karni',
       'kamlesh ko baap'

       ]
trainer=ListTrainer(bot)
trainer.train(convo)
# print('talk to bot')
# while True:
#        query=input()
#        if query=='exit':
#               break
#        answer=bot.get_response(query)
#        print('bot:',answer)
main=Tk()

main.geometry('500x500')
main.title('my bot')
img=PhotoImage(file="bot.png")
photoL=Label(main,image=img,width=80,height=80)
photoL.pack(pady=10)
#take query: take input from user and convert into string
def takeQuery():
    sr=s.Recognizer()
    sr.pause_threshold=1
    print('your bot listening')
    with s.Microphone() as m:
       try:
           audio = sr.listen(m)
           query = sr.recognize_google(audio, language='eng-in')
           print(query)
           text.delete(0, END)
           text.insert(0, query)
           ask_from_bot()
       except Exception as e:
           print(e)
           print('not recognize')

def ask_from_bot():
    query=text.get()
    answer_from_bot=bot.get_response(query)
    msgs.insert(END,'you :'+ query)
    msgs.insert(END,"bot :"+str(answer_from_bot))
    speak(answer_from_bot)
    text.delete(0,END)
    msgs.yview(END)

frame=Frame(main)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=15,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH)
frame.pack()
#creating text field
text=Entry(main,font=('verdana',20))
text.pack(fill=X,pady=5)
btn=Button(main,text="ask from bot",command=ask_from_bot)
btn.pack()
def enter_function(event):
    btn.invoke()
#going to bind main window with enter key
main.bind('<Return>',enter_function)

def repeat():
    while True:
        takeQuery()

t=threading.Thread(target=repeat)
t.start()
main.mainloop()


