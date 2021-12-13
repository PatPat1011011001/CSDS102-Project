import tkinter
from tkinter import Frame, font
from tkinter.constants import BOTH, BOTTOM, COMMAND, INSERT, LEFT, NONE, RIGHT, TOP
from typing import Text
import tkinter as tk
from tabulate import tabulate
import os
import math
import numpy as np #pip install numpy

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

#TITLE
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
    
    xpx_out_1_round = round(xPx_Out_1, 2)
    xpx_out_2_round = round(xPx_Out_2, 2)
    xpx_out_3_round = round(xPx_Out_3, 2)
    xpx_out_4_round = round(xPx_Out_4, 2)


    x2_1  = float(txtbox_ValueX1.get("1.0","end-1c")) * float(txtbox_ValueX1.get("1.0","end-1c"))
    x2_2  = float(txtbox_ValueX2.get("1.0","end-1c")) * float(txtbox_ValueX2.get("1.0","end-1c"))
    x2_3  = float(txtbox_ValueX3.get("1.0","end-1c")) * float(txtbox_ValueX3.get("1.0","end-1c"))
    x2_4  = float(txtbox_ValueX4.get("1.0","end-1c")) * float(txtbox_ValueX4.get("1.0","end-1c"))
    
    x2Px_1 = x2_1 * float(txtbox_ValuePx1.get("1.0","end-1c"))
    x2Px_2 = x2_2 * float(txtbox_ValuePx2.get("1.0","end-1c"))
    x2Px_3 = x2_3 * float(txtbox_ValuePx3.get("1.0","end-1c"))
    x2Px_4 = x2_4 * float(txtbox_ValuePx4.get("1.0","end-1c"))
    
    x2Px_1_round = round(x2Px_1, 2)
    x2Px_2_round = round(x2Px_2, 2)
    x2Px_3_round = round(x2Px_3, 2)
    x2Px_4_round = round(x2Px_4, 2)
    
    

    Px_Total = float(txtbox_ValuePx1.get("1.0","end-1c")) + float(txtbox_ValuePx2.get("1.0","end-1c")) + float(txtbox_ValuePx3.get("1.0","end-1c")) + float(txtbox_ValuePx4.get("1.0","end-1c"))
    xPx_Total =  float(xPx_Out_1) + float(xPx_Out_2) + float(xPx_Out_3) + float(xPx_Out_4)
    x2px_Total = '\u03A3[x\u00b2P(x)] = ', float(x2Px_1) + float(x2Px_2) + float(x2Px_3) + float(x2Px_4)
    

    Mean_Inp = xPx_Total
    Mean_Out = "Mean: \u03A3[xP(x)] = " + str(Mean_Inp)
    Variance_xPxT = xPx_Out_1 + xPx_Out_2 + xPx_Out_3 + xPx_Out_4
    Variance_x2pxT =  x2Px_1 + x2Px_2 + x2Px_3 + x2Px_4
    Variance_inp = Variance_x2pxT - Variance_xPxT**2
    Variance_Round = round(Variance_inp, 2)
    Variance_out = "Variance: \u03A3[x\u00b2P(x)] - \u03A3[xP(x)]\u00b2 = " + str(Variance_Round)

    STD_inp = np.sqrt(Variance_inp)
    STD_round = round(STD_inp, 2)
    STD_out = "STD: " + str(STD_round)

    #Table with TIBULATE 
    table = [['x', 'P(x)', 'xP(x)', 'x\u00b2', 'x\u00b2P(x)'],  [txtbox_ValueX1.get("1.0","end-1c"), txtbox_ValuePx1.get("1.0","end-1c"), xpx_out_1_round, x2_1, x2Px_1_round], [txtbox_ValueX2.get("1.0","end-1c"), txtbox_ValuePx2.get("1.0","end-1c"),  xpx_out_2_round, x2_2, x2Px_2_round], [txtbox_ValueX3.get("1.0","end-1c"), txtbox_ValuePx3.get("1.0","end-1c"),  xpx_out_3_round, x2_3, x2Px_3_round], [txtbox_ValueX4.get("1.0","end-1c"), txtbox_ValuePx4.get("1.0","end-1c"), xpx_out_4_round, x2_4, x2Px_4_round],[" ", Px_Total, xPx_Total, " ", x2px_Total]]
    
    
    txtbox_Result=tk.Text(Result, height=15, width=70)
    txtbox_Result.pack()
    print = tabulate(table, headers='firstrow', tablefmt='grid')
    txtbox_Result.insert(INSERT, print)
    txtbox_Result.configure(state='disabled', font=("courier", 12)) #Disable TextBox from Editing and Read only
    
    #Print Mean, variance, and std
    Lbl_Mean = tkinter.Label(Result, text=Mean_Out, font=("Time New Roman", 16)).pack()
    Lbl_Variance = tkinter.Label(Result, text=Variance_out, font=("Time New Roman", 16)).pack()
    Lbl_STD = tkinter.Label(Result, text=STD_out, font=("Time New Roman", 16)).pack()
    
    Btn_Back = tkinter.Button(Result, text="Back", command = Result.destroy).pack()


#Main Button
Btn_Result = tkinter.Button(Bottomframe, text="Show Result", height=10, width=40, command = Result_Gui).pack(side=TOP, pady=10)

#Main and Start
main.mainloop()
