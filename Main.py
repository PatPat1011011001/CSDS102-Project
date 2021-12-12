import tkinter
from tkinter import Frame, font
from tkinter.constants import BOTH, BOTTOM, COMMAND, INSERT, LEFT, NONE, RIGHT, TOP
from typing import Text
import tkinter as tk
from tabulate import tabulate
import os
import math

#Main Menu Tkinter GUI
main = tkinter.Tk()
main.title("CSDS102-Project")
main.geometry('650x600')

#String and Data Type
ds = "\u03B4"

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


def Result_Gui():
        #New WIndows
    global Result
    Result = tkinter.Tk()
    Result.title("CSDS102-Project2")
    Result.geometry('850x550')

    #Math_Process
    xPx_Out_1 = float(txtbox_ValueX1.get("1.0","end-1c")) * float(txtbox_ValuePx1.get("1.0","end-1c"))
    xPx_Out_2 = float(txtbox_ValueX2.get("1.0","end-1c")) * float(txtbox_ValuePx2.get("1.0","end-1c"))
    xPx_Out_3 = float(txtbox_ValueX3.get("1.0","end-1c")) * float(txtbox_ValuePx3.get("1.0","end-1c"))
    xPx_Out_4 = float(txtbox_ValueX4.get("1.0","end-1c")) * float(txtbox_ValuePx4.get("1.0","end-1c"))

    x2_1  = float(txtbox_ValueX1.get("1.0","end-1c")) * float(txtbox_ValueX1.get("1.0","end-1c"))
    x2_2  = float(txtbox_ValueX2.get("1.0","end-1c")) * float(txtbox_ValueX2.get("1.0","end-1c"))
    x2_3  = float(txtbox_ValueX3.get("1.0","end-1c")) * float(txtbox_ValueX3.get("1.0","end-1c"))
    x2_4  = float(txtbox_ValueX4.get("1.0","end-1c")) * float(txtbox_ValueX4.get("1.0","end-1c"))

    x2Px_1 = x2_1 * float(txtbox_ValuePx1.get("1.0","end-1c"))
    x2Px_2 = x2_2 * float(txtbox_ValuePx2.get("1.0","end-1c"))
    x2Px_3 = x2_3 * float(txtbox_ValuePx3.get("1.0","end-1c"))
    x2Px_4 = x2_4 * float(txtbox_ValuePx4.get("1.0","end-1c"))

    Px_Total = float(txtbox_ValuePx1.get("1.0","end-1c")) + float(txtbox_ValuePx2.get("1.0","end-1c")) + float(txtbox_ValuePx3.get("1.0","end-1c")) + float(txtbox_ValuePx4.get("1.0","end-1c"))
    xPx_Total = '\u03A3[xP(x)] = ', float(xPx_Out_1) + float(xPx_Out_2) + float(xPx_Out_3) + float(xPx_Out_4)
    x2px_Total = '\u03A3[x\u00b2P(x)] = ', float(x2Px_1) + float(x2Px_2) + float(x2Px_3) + float(x2Px_4)
    

    Mean_Out ="Mean: ", xPx_Total
    Variance_xPxT = xPx_Out_1 + xPx_Out_2 + xPx_Out_3 + xPx_Out_4
    Variance_x2pxT =  x2Px_1 + x2Px_2 + x2Px_3 + x2Px_4
    Variance_Out ="Variance: ", Variance_x2pxT - (Variance_xPxT**2)
    STD_inp = math.sqrt(float(Variance_Out))
    STD_out = "STD: ", str(STD_inp)

    #Table with TIBULATE 
    table = [['x', 'P(x)', 'xP(x)', 'x\u00b2', 'x\u00b2P(x)'],  [txtbox_ValueX1.get("1.0","end-1c"), txtbox_ValuePx1.get("1.0","end-1c"), xPx_Out_1, x2_1, x2Px_1 ], [txtbox_ValueX2.get("1.0","end-1c"), txtbox_ValuePx2.get("1.0","end-1c"),  xPx_Out_2, x2_2, x2Px_2], [txtbox_ValueX3.get("1.0","end-1c"), txtbox_ValuePx3.get("1.0","end-1c"),  xPx_Out_3, x2_3, x2Px_3], [txtbox_ValueX4.get("1.0","end-1c"), txtbox_ValuePx4.get("1.0","end-1c"), xPx_Out_4, x2_4, x2Px_4],[" ", Px_Total, xPx_Total, " ", x2px_Total]]
    
    
    txtbox_Result=tk.Text(Result, height=20, width=80)
    txtbox_Result.pack()
    print = tabulate(table, headers='firstrow', tablefmt='grid')
    txtbox_Result.insert(INSERT, print)

    #mean variance and std
    Lbl_Mean = tkinter.Label(Result, text=Mean_Out, font=("Time New Roman", 16)).pack()
    Lbl_Variance = tkinter.Label(Result, text=Variance_Out, font=("Time New Roman", 16)).pack()
    Lbl_STD = tkinter.Label(Result, text=STD_out, font=("Time New Roman", 16)).pack()
    
    txtbox_Result.configure(state='disabled', font=("courier", 12)) #Disable TextBox from Editing and Read only
    Btn_Back = tkinter.Button(Result, text="Back", command = Result.destroy).pack()


#Main Button
Btn_Result = tkinter.Button(Bottomframe, text="Show Result", height=10, width=40, command = Result_Gui).pack(side=TOP, pady=10)

#Main and Start
main.mainloop()
