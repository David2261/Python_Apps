#import the necessary libraries
import tkinter
from tkinter import *
from tkinter import messagebox

val=""
A = 0
operator=""

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def btn_add_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def btn_sub_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def btn_mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_equal_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "="
    val = val + "="
    data.set(val)

def C_pressed():
    global A
    global operator
    global val
    val = ""
    A=0
    operator=""
    data.set(val)


def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x=int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val=str(c)
    elif operator == "-":
        x=int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val=str(c)
    elif operator == "*":
        x=int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val=str(c)
    elif operator == "/":
        x=int((val2.split("/")[1]))
        if x==0:
            messagebox.showerror("Error","Division by 0 Not Allowed")
            A==""
            val=""
            data.set(val)
        else:
            c=int(A/x)
            data.set(c)
            val=str(c)

#create a root window
root = tkinter.Tk()
#set geometry
root.geometry("250x400+300+300")
#disable the resize option for better UI
root.resizable(0,0)
#Give the tiltle to your calculator window
root.title("Investor-Cal")


#Label
data= StringVar()
lbl=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Verdana",20),
    textvariable=data,
    background="#ffffff",
    fg="#000000",
)
#expand option deals with the expansion of parent widget.
lbl.pack(expand=True,fill="both",)


#Frame Coding for Buttons
#Frame for root window
#Frame 1
btnrow1=Frame(root,bg="pink")
#If frame gets some space it can expand
btnrow1.pack(expand=True,fill="both",)

#Frame 2
btnrow2=Frame(root)
btnrow2.pack(expand=True,fill="both",)

#Frame 3
btnrow3=Frame(root)
btnrow3.pack(expand=True,fill="both",)

#Frame 4
btnrow4=Frame(root)
btnrow4.pack(expand=True,fill="both",)


#Button row One
#Button 1
btn1=Button(
    btnrow1,
    text = "1",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_1_isclicked,
)
#Buttons will be side by side
btn1.pack(side=LEFT,expand=True,fill="both",)

#Button 2
btn2=Button(
    btnrow1,
    text = "2",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_2_isclicked,
)
#Buttons will be side by side
btn2.pack(side=LEFT,expand=True,fill="both",)

#Button 3
btn3=Button(
    btnrow1,
    text = "3",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_3_isclicked,
)
#Buttons will be side by side
btn3.pack(side=LEFT,expand=True,fill="both",)

#Button add
btnadd=Button(
    btnrow1,
    text = "+",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_add_clicked,
)
#Buttons will be side by side
btnadd.pack(side=LEFT,expand=True,fill="both",)

#Button row Two
#Button 4
btn4=Button(
    btnrow2,
    text = "4",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_4_isclicked,
)
#Buttons will be side by side
btn4.pack(side=LEFT,expand=True,fill="both",)

#Button 5
btn5=Button(
    btnrow2,
    text = "5",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_5_isclicked,
)
#Buttons will be side by side
btn5.pack(side=LEFT,expand=True,fill="both",)

#Button 6
btn6=Button(
    btnrow2,
    text = "6",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_6_isclicked,
)
#Buttons will be side by side
btn6.pack(side=LEFT,expand=True,fill="both",)

#Button Subtraction
btnsub=Button(
    btnrow2,
    text = "-",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_sub_clicked,
)
#Buttons will be side by side
btnsub.pack(side=LEFT,expand=True,fill="both",)

#Button row Three
#Button 7
btn7=Button(
    btnrow3,
    text = "7",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_7_isclicked,
)
#Buttons will be side by side
btn7.pack(side=LEFT,expand=True,fill="both",)

#Button 8
btn8=Button(
    btnrow3,
    text = "8",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_8_isclicked,
)
#Buttons will be side by side
btn8.pack(side=LEFT,expand=True,fill="both",)

#Button 9
btn9=Button(
    btnrow3,
    text = "9",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_9_isclicked,
)
#Buttons will be side by side
btn9.pack(side=LEFT,expand=True,fill="both",)

#Button Multiply
btnmul=Button(
    btnrow3,
    text = "*",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_mul_clicked,
)
#Buttons will be side by side
btnmul.pack(side=LEFT,expand=True,fill="both",)

#Button row Four
#Button C
btnC=Button(
    btnrow4,
    text = "C",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = C_pressed,
)
#Buttons will be side by side
btnC.pack(side=LEFT,expand=True,fill="both",)

#Button 0
btn0=Button(
    btnrow4,
    text = "0",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_0_isclicked,
)
#Buttons will be side by side
btn0.pack(side=LEFT,expand=True,fill="both",)

#Button Equal to
btnequal=Button(
    btnrow4,
    text = "=",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command=result,
)
#Buttons will be side by side
btnequal.pack(side=LEFT,expand=True,fill="both",)

#Button Divide
btndiv=Button(
    btnrow4,
    text = "/",
    font = ("Verdana",22),
    relief =GROOVE,
    border=0,
    command = btn_div_clicked,
    
)
#Buttons will be side by side
btndiv.pack(side=LEFT,expand=True,fill="both",)


root.mainloop()