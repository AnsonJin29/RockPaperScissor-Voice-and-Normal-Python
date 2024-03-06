#make computer question mark image
#once reset clear radio button
#final touches no bugs

import random
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk
import speech_recognition
import pyttsx3
window=ThemedTk(theme='equilux')
window.configure(themebg='equilux')
window.geometry('500x420')
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
rdbtn=StringVar() #unlike '' StaringVar command keeps rdbtn a string the whole time and cant change


def reset():
    global playerPoint,pcPoint

    rdbtn.set(None)
    rad1.place_forget()
    rad2.place_forget()
    rad3.place_forget()
    resetBut.place_forget()

    start.place(x=110, y=285)
    userScore.place(x=175, y=140)
    user.configure(image=qm)
    pc.configure(image=qm)
    playerPoint=0
    pcPoint=0
    userScore.configure(text=playerPoint)
    pcScore.configure(text=pcPoint)

    description.configure(text='Click the start button and select your input (Rock, Paper or Scissor)\n    once selected the PC will automatically respond with a random\n                  choice and whoever wins will get +1 point')

def randomAns():
    global result, choice
    choice=random.choice(['rock.png','paper.png','scissor.png'])
    result=PhotoImage(file=choice)
    return result

def system():
    global pcImage, choice, playerPoint, pcPoint
    if (player==1 and choice=='rock.png') or (player==2 and choice=='paper.png') or (player==3 and choice=='scissor.png'):
        description.configure(text='Its a draw and no one wins')
    elif (player==2 and choice=='rock.png') or (player==3 and choice=='paper.png') or (player==1 and choice=='scissor.png'):
        description.configure(text='You won! one point added to player')
        playerPoint+=1
        userScore.configure(text=playerPoint)
        if playerPoint>=20:
            userScore.place(x=165,y=140)
        if playerPoint>=100:
            userScore.place(x=155,y=140)
    elif (player==3 and choice=='rock.png') or (player==1 and choice=='paper.png') or (player==2 and choice=='scissor.png'):
        description.configure(text='You lost! one point added to the computer')
        pcPoint+=1
        pcScore.configure(text=pcPoint)
        if pcPoint>=100:
            pcScore.place(x=265,y=140)
    else:
        description.configure(text='An error has occured, please try again')


def init(*args):
    global running, player, pcImage
    rad1.place(x=140, y=250)
    rad2.place(x=210, y=250)
    rad3.place(x=280, y=250)
    resetBut.place(x=110, y=315)
    start.place_forget()

    if rdbtn.get()=='radio1':
        user.configure(image=rockI)
        player=1
        pc.configure(image=randomAns())
        system()
    if rdbtn.get()=='radio2':
        user.configure(image=paperI)
        player=2
        pc.configure(image=randomAns())
        system()
    if rdbtn.get()=='radio3':
        user.configure(image=scissor1)
        player=3
        pc.configure(image=randomAns())
        system()



#UI-------------------------------------------------------------------------------


title=ttk.Label(window,text='Rock Paper Scissor',font=('Agency FB Bold',35))
title.place(x=100,y=5)

start=ttk.Button(window,text='Start Game',command=init,width=40)
start.place(x=110,y=285)

resetBut=ttk.Button(window,text='Reset',command=reset,width=40)


user=ttk.Label(window,image=qm)
user.place(x=40,y=90)

userText=ttk.Label(window,text='Player',font=('Agency FB Bold',15))
userText.place(x=70,y=260)

userScore=ttk.Label(window,text=playerPoint,font=('Agency FB Bold',50))
userScore.place(x=175,y=140)

pcScore=ttk.Label(window,text=pcPoint,font=('Agency FB Bold',50))
pcScore.place(x=275,y=140)

colon=ttk.Label(window,text=':',font=('Agency FB Bold',50))
colon.place(x=235,y=135)

pcText=ttk.Label(window,text='Computer',font=('Agency FB Bold',15))
pcText.place(x=370,y=260)

pc=ttk.Label(window,image=qm)
pc.place(x=345,y=90)

rdbtn.trace('w',init)
rad1=ttk.Radiobutton(window,text='Rock',value='radio1',variable=rdbtn)

rad2=ttk.Radiobutton(window,text='Paper',value='radio2',variable=rdbtn)

rad3=ttk.Radiobutton(window,text='Scissor',value='radio3',variable=rdbtn)

description=ttk.Label(window,text='Click the start button and select your input (Rock, Paper or Scissor)\n    once selected the PC will automatically respond with a random\n                  choice and whoever wins will get +1 point')
description.place(x=70,y=350)


window.mainloop()