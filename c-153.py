from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Testing Random Function")
root.geometry("600x600")
root.config(bg="#729fe8")

ibox=Entry(root)
ibox.place(relx=0.5,rely=0.3,anchor=CENTER)

inputlabel=Label(root)
inputlabel.place(relx=0.5,rely=0.4,anchor=CENTER)

outputlabel=Label(root)
outputlabel.place(relx=0.5,rely=0.6,anchor=CENTER)

sample3d=[[['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],["Book","Food","Nature","Art","World"],["!","@","#","$","%","&","?"]]]

def password():
    inputlabel["text"]="Guessed Password is : "+ibox.get()
    
    r1=random.randint(0,25)
    r2=random.randint(0,4)
    r3=random.randint(0,6)
    
    outputlabel["text"]="Generated Password is : "+sample3d[0][0][r1]+sample3d[0][1][r2]+sample3d[0][2][r3]


btn=Button(root,text="Generate",command=password)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()