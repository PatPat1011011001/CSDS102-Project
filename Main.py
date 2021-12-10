import tkinter
from tkinter.constants import COMMAND, INSERT
from typing import Text
import tkinter as tk
from tabulate import tabulate
import os

main = tkinter.Tk()
main.title("CSDS102-Project")
main.geometry('850x550')

ds = "\u03B4"
table = [['x', 'P(x)', 'x\u00b2', 'x\u00b2*P(x)'],  [ds, 'Jane', 25, 56], ['Jennifer', 'Doe', 28, 45]]

#print(tabulate(table, headers='firstrow', tablefmt='grid'))

#Function
def test():
    print = tabulate(table, headers='firstrow', tablefmt='grid')
    textExample.insert(INSERT, print)
    textExample.configure(state='disabled') #Disable TextBox from Editing and Read only

def test2():
    textExample.configure(state='normal') #Enable TextBox from Write Only
    textExample.delete("1.0", "end")

#UI
Bt1 = tkinter.Button(main, text="Test", command = test).pack()
Bt2 = tkinter.Button(main, text="normal", command = test2).pack()

textExample=tk.Text(main, height=100, width=100)
textExample.pack()


#Main
main.mainloop()
