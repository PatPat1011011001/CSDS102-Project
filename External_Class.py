import tkinter
from tkinter import font
from tkinter.constants import COMMAND, INSERT
from typing import Text
import tkinter as tk
from tabulate import tabulate
import os

#Main Menu Tkinter GUI
main = tkinter.Tk()
main.title("CSDS102-Project")
main.geometry('850x550')


#String and Data Type
ds = "\u03B4"

#Table with TIBULATE 
table = [['x', 'P(x)', 'x\u00b2', 'x\u00b2*P(x)'],  [ds, 'Jane', 25, 56], ['Jennifer', 'Doe', 28, 45]]

#print(tabulate(table, headers='firstrow', tablefmt='grid'))

#Function UI

Title_Main = tkinter.Label(main, text= table)
Title_Main.configure(font=("courier", 14))

Title_Main.pack()

#Closing 

#Main and Start
main.mainloop()
