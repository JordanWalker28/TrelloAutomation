import tkinter as tk
from tkinter import ttk

OptionList = [
"Aries",
"Taurus",
"Gemini",
"Cancer"
] 

def clickMe():
    label.configure(text= 'Hello ' + name.get())

def clearTextInput():
    textExample.delete("1.0","end")

app = tk.Tk()

app.geometry('300x400')

variable = tk.StringVar(app)
variable.set(OptionList[0])

opt = tk.OptionMenu(app, variable, *OptionList)
opt.config(width=2, font=('Helvetica', 12))
opt.grid(column = 0, row = 0)

label = ttk.Label(app, text = "Enter Your Name")
label.grid(column = 0, row = 1)

name = tk.StringVar()
nameEntered = ttk.Entry(app, width = 2, textvariable = name)
nameEntered.grid(column = 0, row = 2)
 
 
button = ttk.Button(app, text = "Click Me", command = clickMe)
button.grid(column= 0, row = 3)

textExample=tk.Text(app, height=10)
textExample.grid(column=0, row =4)
btnRead=tk.Button(app, height=1, text="Clear", command=clearTextInput)
btnRead.grid(column=0, row =5)

app.mainloop()
