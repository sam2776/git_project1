from tkinter import *
from datetime import datetime

root = Tk()
root.title("Время для гимнастики")

def updare_time():
    format = '%H:%M:%S'
    now = (datetime.now()).strftime(format)
    s2 = '18:2:59'
    string = datetime.strptime(s2, format) - datetime.strptime(now, format)
    l.config(text= string)
    l.after(1000,updare_time)

l = Label(root, font=('calidri',50,'bold'), background='green', foreground='white')
l.pack(anchor='center')
updare_time()
mainloop()

