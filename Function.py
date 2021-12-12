import tkinter
from tkinter import Frame, font
from tkinter.constants import BOTH, BOTTOM, COMMAND, INSERT, LEFT, NONE, RIGHT, TOP
from typing import Text
import tkinter as tk
from tabulate import tabulate
import os

#Main Menu Tkinter GUI
main = tkinter.Tk()
main.title("CSDS102-Project")
main.geometry('650x600')

#FRAME
frame = Frame(main)
frame.pack()

Leftframe = Frame(main, bd=50)
Leftframe.pack(side=LEFT)

Rightframe = Frame(main, bd=50)
Rightframe.pack(side=RIGHT)

Bottomframe = Frame(main)
Bottomframe.pack(side=BOTTOM)

Title_Main = tkinter.Label(frame, text="Calculate of Mean, Variance, and Standard Deviation", font=("Time New Roman", 16))
Title_Main.pack(side=TOP)

#input Value X and Title
Xtitle = tkinter.Label(Leftframe, text="X", font=("Time New Roman", 16))
Xtitle.pack(side=TOP, pady=15, padx=25)
txtbox_ValueX1=tk.Text(Leftframe, width=10, height=1)
txtbox_ValueX1.pack(side=TOP, pady=10, padx=25)
txtbox_ValueX2=tk.Text(Leftframe, width=10, height=1)
txtbox_ValueX2.pack(side=TOP, pady=10, padx=25)
txtbox_ValueX3=tk.Text(Leftframe, width=10, height=1)
txtbox_ValueX3.pack(side=TOP, pady=10, padx=25)
txtbox_ValueX4=tk.Text(Leftframe, width=10, height=1)
txtbox_ValueX4.pack(side=TOP, pady=10, padx=25)
txtbox_ValueX5=tk.Text(Leftframe, width=10, height=1)
txtbox_ValueX5.pack(side=TOP, pady=10, padx=25)

#Input Value of P(x)
PxTitle = tkinter.Label(Rightframe, text="P(x)", font=("Time New Roman", 16))
PxTitle.pack(side=TOP, pady=15, padx=25)
txtbox_ValuePx1=tk.Text(Rightframe, width=10, height=1)
txtbox_ValuePx1.pack(side=TOP, pady=10, padx=25)
txtbox_ValuePx2=tk.Text(Rightframe, width=10, height=1)
txtbox_ValuePx2.pack(side=TOP, pady=10, padx=25)
txtbox_ValuePx3=tk.Text(Rightframe, width=10, height=1)
txtbox_ValuePx3.pack(side=TOP, pady=10, padx=25)
txtbox_ValuePx4=tk.Text(Rightframe, width=10, height=1)
txtbox_ValuePx4.pack(side=TOP, pady=10, padx=25)
txtbox_ValuePx5=tk.Text(Rightframe, width=10, height=1)
txtbox_ValuePx5.pack(side=TOP, pady=10, padx=25)

#Main Button
Btn_Result = tkinter.Button(Bottomframe, text="Show Result", height=10, width=40, command = "Result_Gui").pack(side=TOP, pady=10)

#Math_Process

#Main and Start
main.mainloop()
