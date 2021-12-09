import tkinter
from tkinter.constants import COMMAND, INSERT
from typing import Text
import tkinter as tk

main = tkinter.Tk()
main.title("CSDS102-Project")
main.geometry('850x550')

#Function
def test():
    textExample.insert(INSERT, "Testing")

#UI
Bt1 = tkinter.Button(main, text="Test", command = test).pack()

textExample=tk.Text(main, height=5, width=5)
textExample.pack()


#Main
main.mainloop()
