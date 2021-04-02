from tkinter import *
from tkinter import ttk
import os
import pygame
 
def TestLogic( n ):
    s = "f" + n + ".png"
    stgImg = PhotoImage(file=s)
    label.configure(image=stgImg)
    label.image = stgImg

    t = "Text "+n
    label1.configure(text = t)
 
root = Tk()
 
root.geometry('500x450')
  
stgImg = PhotoImage(file="f1.png")
label=ttk.Label(root, image=stgImg)
label.place(x=0, y=0)
label1=ttk.Label(root, text="Text 1",font = ("Arial", 30))
label1.place(x=200, y=400)


root.after(4500, TestLogic,"2")
root.after(5800, TestLogic,"3")
root.after(6600, TestLogic,"4")
root.after(7500, TestLogic,"5")
root.after(8400, TestLogic,"6")

pygame.mixer.init()
pygame.mixer.music.load("Eminem-FACK (mp3cut.net).mp3")
pygame.mixer.music.play()

root.mainloop()
