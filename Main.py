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

#Result Tkinter GUI
Result = tkinter.Tk()
Result.title("CSDS102-Project")
Result.geometry('850x550')

#String and Data Type
ds = "\u03B4"

#Table with TIBULATE 
table = [['x', 'P(x)', 'x\u00b2', 'x\u00b2*P(x)'],  [ds, 'Jane', 25, 56], ['Jennifer', 'Doe', 28, 45]]

#print(tabulate(table, headers='firstrow', tablefmt='grid'))

#Function UI
def Main_Menu():
    Title_Main = tkinter.Label(main, text="HELLO")
    Title_Main.configure(font=("courier", 14))
    Btn_Result = tkinter.Button(main, text="Show Result", command = Result_Gui).pack()

def Result_Gui():
    txtbox_Result=tk.Text(main, height=100, width=100)
    txtbox_Result.pack()
    print = tabulate(table, headers='firstrow', tablefmt='grid')
    txtbox_Result.insert(INSERT, print)
    txtbox_Result.configure(state='disabled') #Disable TextBox from Editing and Read only
    Btn_Back = tkinter.Button(main, text="Back", command = Main_Menu).pack()

    Result.mainloop()

#Closing 

#Main and Start
main.mainloop()
