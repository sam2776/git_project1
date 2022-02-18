import os
from tkinter import *
from tkinter import messagebox
from random import choice, randrange
from copy import deepcopy
import time

def on_closing():
    global app_running
    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
        app_running = False
        #tk.destroy()

tk=Tk()
def start():
    os.system('python timei.py')




canvas = Canvas(tk, width=800, height=531, bg="red", highlightthickness=0, )

img_obj1 = PhotoImage(file="cloack.png")
canvas.create_image(0, 0, anchor=NW, image=img_obj1)

startBt=Button(tk, text= "Начать отщёт до гимнастики для глаз", command= start, bg="#88c3ff")



canvas.pack()
startBt.place(x=290, y=220, width= 220, height= 50)
tk.mainloop()