import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

root = tk.Tk()
root.title("Calculator")

def calc(key):
    if key == '=':
        available = "/*-+.0123456789"
        if calcEntry.get()[0] not in available:
            calcEntry.insert (tk.END, "First character is not a numeral.")
            messagebox.showerror("Error!", "You entered not a numeral!")
        try:
            result = eval(calcEntry.get())
            calcEntry.insert(tk.END, ' = ' + str(result))
        except:
            result = 0
            calcEntry.insert(tk.END, ' // Error!')
            messagebox.showerror("Error!", "Check the accuracy of entered data.")

    elif key == 'C':
        calcEntry.delete(0, tk.END)

    elif key == '+/-':
        if "=" in calcEntry.get():
            calcEntry.delete(0, tk.END)
        try:
            if calcEntry.get()[0] == '-':
                calcEntry.delete(0)
            else:
                calcEntry.insert(0, '-')
        except IndexError:
            pass
    elif key == '>>':
        calcEntry.delete(-1)
    elif key == '√':
        calcEntry.insert(tk.END, '**(1/2)')
    else:
        if '=' in calcEntry.get():
            calcEntry.delete(0, tk.END)
        calcEntry.insert(tk.END, key)

buttons = [
    '>>' , 'C' , '√', '/',
    '7' , '8' , '9', '*',
    '4' , '5' , '6', '-',
    '1' , '2' , '3', '+',
    '+/-', '0' , '.', '='
]

r = 1
c = 0

for btn in buttons:
    rel = ""
    cmd = lambda x=btn: calc(x)
    ttk.Button(root, text=btn, command=cmd).grid(row=r,column=c)
    c += 1
    if c > 3:
        r += 1
        c = 0

calcEntry = tk.Entry(root,width=50)
calcEntry.grid(row=0,column=0,columnspan=5)
root.mainloop()