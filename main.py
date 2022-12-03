from tkinter import *
import tkinter
import time
import random

m = tkinter.Tk()

buttonMap = {}
row = 3
column = 5
red = True





'''def makeActive(buttonDetail):
    buttonDetail[0].config(bg= "red")
    print(buttonDetail[0])
    m.after(ms=200 ,func=makeActive(buttonDetail))

def removeActive(buttonDetail):
    buttonDetail[0].config(bg= "white")
    m.after(ms=200, func=removeActive(buttonDetail))'''





for i in range(row):
    for j in range(column):
        mybutton= Button(m, text="              ")
        mybutton.grid(row=i, column=j)
        buttonMap[mybutton] = (i, j)




def makeActive(buttonDetail):
    buttonDetail[0].config(bg= "red", command=clicked)

def doNothing():
    pass

def clicked():
    print("clicked")
    buttonDetail[0].config(bg= "white", command=doNothing)
    #buttonDetail = random.choice(list(buttonMap.items()))



for i in range(4):
    buttonDetail = random.choice(list(buttonMap.items()))
    makeActive(buttonDetail)
    #removeActive(buttonDetail)

m.mainloop()



    