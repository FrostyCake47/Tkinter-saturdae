from tkinter import *
import tkinter
import time
import random

m = tkinter.Tk()

buttonMap = {}
row = 3
column = 5
red = True


def removeActive(buttonDetail):
    buttonDetail[0].config(bg= "white")
    m.after(ms=200, func=removeActive(buttonDetail))

'''def makeActive(prevBlock= None):

    buttonDetail = random.choice(list(buttonMap.items()))

    buttonDetail[0].config(bg= "red")
    prevBlock = buttonDetail
    prevBlock[0].config(bg = "white")
    print(buttonDetail[0])
    m.after(ms=200 ,func=makeActive(prevBlock))'''

def makeActive(prevBlock= None):

    buttonDetail = random.choice(list(buttonMap.items()))

    buttonDetail[0].config(bg= "red")
    print(buttonDetail[0])
    m.after(ms=200 ,func=makeActive)

for i in range(row):
    for j in range(column):
        mybutton= Button(m, text="              ")
        mybutton.grid(row=i, column=j)
        buttonMap[mybutton] = (i, j)

makeActive()

m.mainloop()



    