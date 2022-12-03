from tkinter import *
from tkinter import messagebox
import tkinter
import time
import random

m = tkinter.Tk()
m.title("QuickShot")

ROW = 5
COLUMN = 5
BOXWIDTH = 15
buttonMap = {}
score = 0

appearable = True

scoreText = Label(m, text = "Score: 0", font =("helvicta", 14))
scoreText.grid(row=0, column=0)
scoreText.pack()

timeLeft =  60
timeText = Label(m, text= "Time: 1:00", font=("helvicta", 14))
timeText.pack()

gamegrid = Frame(m)
gamegrid.pack(side=BOTTOM)

for i in range(ROW):
    for j in range(COLUMN):
        mybutton= Button(gamegrid, text=" "*BOXWIDTH)
        mybutton.grid(row=i+1, column=j)
        buttonMap[mybutton] = (i+1, j)

def removeFunc():
    pass

def makeActive(buttonDetail):
    buttonDetail[0].config(bg= "red")
    m.after(ms=200 ,func=makeActive(buttonDetail))

def countdown(count):   
    timeText['text'] = "Time: "+ str(count)
    if count > 0:
        m.after(1000, countdown, count-1)
    else:
        messagebox.showinfo("Game Over!", "Score: " + str(score))
        m.quit()
        

def onCLick():
    global appearable
    global score
    global scoreText

    buttonDetail[0].config(bg = "white", command= removeFunc)
    score += 1
    appearable = True
    stext = "Score: " + str(score)
    scoreText.config(text=stext)

    game()

def game():
    global appearable
    global buttonDetail

    if appearable:
        print(buttonDetail[0])
        buttonDetail = random.choice(list(buttonMap.items()))
        buttonDetail[0].config(bg= "red", command=onCLick)
        appearable = False


def main():
    global buttonDetail
    global appearable
    count = 30

    buttonDetail = random.choice(list(buttonMap.items()))
    appearable = True
    countdown(count)
    game()
    m.mainloop()

if __name__ == "__main__":
    main()
