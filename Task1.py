import os
import tkinter as tk  
from tkinter import ttk
  
win = tk.Tk()# Application Name  
win.title("Python Task : 1")# Label  
lbl = ttk.Label(win, text = "Enter aplication name u want to open:").grid(column = 0, row = 0)# Click event

def click():   
  while True:
    userinput = name.get()
    # os.system(userinput)
    if("run" in userinput) or ("google" in userinput) and ("chrome" in userinput):
      os.system("chrome")
    elif(("run" in userinput)or("open" in userinput)or("execute" in userinput)) and ("notepad" in userinput):
      os.system("notepad")
    elif(("run" in userinput) or ("open" in userinput) or ("execute" in userinput)) and ("paint in userinput"):
      os.system("mspaint")
    elif(("run" in userinput) or ("open" in userinput) or ("execute" in userinput)) and ("wordpad in userinput"):
      os.system("wordpad")
    elif(("run" in userinput) or ("open" in userinput) or ("execute" in userinput)) and ("media" in userinput) and ("player" in userinput):
      os.system("wmplayer")
    elif("exit" in userinput) or ("quit" in userinput):
      break
  else:
    print("Not valid")
    break
  

name = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 22, textvariable = name).grid(column = 0, row = 1)# Button widget  
button = ttk.Button(win, text = "submit", command = click).grid(column = 1, row = 1)  
win.mainloop()   
