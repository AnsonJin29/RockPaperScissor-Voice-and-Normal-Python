#finish pc response
#decide who wins
#record rounds

import random
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk
import speech_recognition
import pyttsx3
window=ThemedTk(theme='equilux')
window.configure(themebg='equilux')
window.geometry('500x400')
window.title('Rock Paper Scissor Voice')
window.resizable(False, False)

rockI=PhotoImage(file='rock.png')
paperI=PhotoImage(file='paper.png')
scissor1=PhotoImage(file='scissor.png')
qm=PhotoImage(file='question.png')
player=0 #0=none 1=rock 2=paper 3=scissors
choice=''
playerPoint=0
pcPoint=0

r=speech_recognition.Recognizer()
def randomAns():
    global result, choice
    choice=random.choice(['rock.png','paper.png','scissor.png'])
    result=PhotoImage(file=choice)
    return result

def system():
    global pcImage, choice, playerPoint, pcPoint
    if (player==1 and choice=='rock.png') or (player==2 and choice=='paper.png') or (player==3 and choice=='scissor.png'):
        speakText('Its a draw and no one wins')
    elif (player==2 and choice=='rock.png') or (player==3 and choice=='paper.png') or (player==1 and choice=='scissor.png'):
        speakText('You won! one point added to player')
        playerPoint+=1
        userScore.configure(text=playerPoint)
    elif (player==3 and choice=='rock.png') or (player==1 and choice=='paper.png') or (player==2 and choice=='scissor.png'):
        speakText('You lost! one point added to the computer')
        pcPoint+=1
        pcScore.configure(text=pcPoint)
    else:
        speakText('An error has occured, please try again')

def speakText(x):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-400)
    engine.say(x)
    engine.runAndWait()
def voice():
    global running, player, pcImage
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2,duration=1)
        speakText('Say Something')
        audio2=r.listen(source2)

        try:
            MyText=r.recognize_google(audio2)
        except:
            speakText('Didnt recognise voice, try again')
            voice()
            return
        MyText=MyText.lower()
        speakText('you said'+MyText)

    if 'rock' in MyText:
        user.configure(image=rockI)
        player=1
        pc.configure(image=randomAns())
        system()
    if 'paper' in MyText:
        user.configure(image=paperI)
        player=2
        pc.configure(image=randomAns())
        system()
    if 'scissor' in MyText or 'scissors' in MyText:
        user.configure(image=scissor1)
        player=3
        pc.configure(image=randomAns())
        system()



#UI-------------------------------------------------------------------------------


title=ttk.Label(window,text='Rock Paper Scissor',font=('Agency FB Bold',35))
title.place(x=100,y=5)

start=ttk.Button(window,text='Start Game',command=voice,width=40)
start.place(x=110,y=290)

user=ttk.Label(window,image=qm)
user.place(x=40,y=90)

userText=ttk.Label(window,text='Player')
userText.place(x=70,y=260)

userScore=ttk.Label(window,text=playerPoint,font=('Agency FB Bold',50))
userScore.place(x=175,y=160)

pcScore=ttk.Label(window,text=pcPoint,font=('Agency FB Bold',50))
pcScore.place(x=275,y=160)

colon=ttk.Label(window,text=':',font=('Agency FB Bold',50))
colon.place(x=235,y=155)

pcText=ttk.Label(window,text='Computer')
pcText.place(x=370,y=260)

pc=ttk.Label(window,image=randomAns())
pc.place(x=345,y=90)


window.mainloop()