import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


root = tk.Tk()
root.title("Калькулятор")

memory = ''

def calc(key):
    global memory
    if key == '=':
        eval(memory)
    else:
        memory += key


buttons = [
    'CE' , 'C' , '<<', '/',
    '7' , '8' , '9', '*',
    '4' , '5' , '6', '-',
    '1' , '2' , '3', '+',
    '+/-', '0' , ',', '='
]

r = 1
c = 0

for btn in buttons:
    tk.rel = ""
    tk.cmd = lambda x=btn: calc(x)
    ttk.Button(root, text=btn).grid(row=r,column=c)
    c += 1
    if c>3:
        r += 1
        c = 0

calcEntry = tk.Entry(root,width=33)
calcEntry.grid(row=0,column=0,columnspan=5)
root.mainloop()