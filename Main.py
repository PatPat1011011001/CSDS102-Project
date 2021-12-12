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
main.geometry('850x600')

#Result Tkinter GUI


#String and Data Type
ds = "\u03B4"

#INPUT DATA
#Value of X Input
ValueXInp_1 = 0
ValueXInp_2 = 0
ValueXInp_3 = 0
ValueXInp_4 = 0
ValueXInp_5 = 0

#Value of P(x)
ValuePxInp_1 = 0
ValuePxInp_2 = 0
ValuePxInp_3 = 0
ValuePxInp_4 = 0
ValuePxInp_5 = 0



#Table with TIBULATE 
table = [['x', 'P(x)', 'x\u00b2', 'x\u00b2*P(x)'],  [ds, 'Jane', 25, 56], ['Jennifer', 'Doe', 28, 45]]

#print(tabulate(table, headers='firstrow', tablefmt='grid'))

#Function UI

def Result_Gui():
        #New WIndows
    global Result
    Result = tkinter.Tk()
    Result.title("CSDS102-Project2")
    Result.geometry('850x550')
    
    txtbox_Result=tk.Text(Result, height=20, width=50)
    txtbox_Result.pack()
    print = tabulate(table, headers='firstrow', tablefmt='grid')
    txtbox_Result.insert(INSERT, print)
    txtbox_Result.configure(state='disabled', font=("courier", 24)) #Disable TextBox from Editing and Read only
    Btn_Back = tkinter.Button(Result, text="Back", command = Result.destroy).pack()




Title_Main = tkinter.Label(main, text="Calculate of Mean, Variance, and Standard Deviation", font=("Time New Roman", 16)).place(x=160, y=0)

#input Value X and Title
Title_Main = tkinter.Label(main, text="X", font=("Time New Roman", 16)).place(x=190, y=50)
txtbox_ValueX1=tk.Text(main, height=2, width=10).place(x=150, y=100)
txtbox_ValueX2=tk.Text(main, height=2, width=10).place(x=150, y=200)
txtbox_ValueX3=tk.Text(main, height=2, width=10).place(x=150, y=300)
txtbox_ValueX4=tk.Text(main, height=2, width=10).place(x=150, y=400)
txtbox_ValueX5=tk.Text(main, height=2, width=10).place(x=150, y=500)

#Input Value of P(x) and Title
Title_Main = tkinter.Label(main, text="P(x)", font=("Time New Roman", 16)).place(x=470, y=50)
txtbox_ValuePx1=tk.Text(main, height=2, width=10).place(x=450, y=100)
txtbox_ValuePx2=tk.Text(main, height=2, width=10).place(x=450, y=200)
txtbox_ValuePx3=tk.Text(main, height=2, width=10).place(x=450, y=300)
txtbox_ValuePx4=tk.Text(main, height=2, width=10).place(x=450, y=400)
txtbox_ValuePx5=tk.Text(main, height=2, width=10).place(x=450, y=500)


#Main Button
Btn_Result = tkinter.Button(main, text="Show Result", height=10, width=20, command = Result_Gui).place(x=650, y=250)

#Math_Process

#Main and Start
main.mainloop()
