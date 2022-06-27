#import "tkinter library" for create GUI
import tkinter as tk
from tkinter import messagebox as mb

from setuptools import Command

#import "Generator" Class
from GenerateClass import Generate_Random_Password

#import "Copy to clipboard" class 
from CopyClass import CopyPass




#Root
Root = tk.Tk()
Root.geometry("300x250")
Root.resizable(width=False, height=False)
Root.title("Password Generator")
Root.config(bg="#1034A6")

#create Output string and set to Result label
Ouput1 = tk.StringVar()
Ouput1.set("it's your Password")


#colors
Iconsbg = "Gold"
Labelsbg = "#420D09"

#entries

Entry1 = tk.Entry(Root,font=("Arial",14),fg=Labelsbg)
Entry1.place(x=20,y=60,height=29,width=155)


#Functions


#Convert the user input to integer for giving input to Generate Function
def Convert():
    number1 = Entry1.get()
    try:
        number1= int(number1)
        return number1
    except:
        return False



#Generate Random Password and set to Label(Output)
def Gen():

    # create object from Generate_Random_class
    test1 = Generate_Random_Password()

    try:
        #this string is output
        ResultStr = test1.generate(Convert())

        if (ResultStr):
            #set Result to Label(Output)

            Ouput1.set(ResultStr)

        else:
            mb.showerror("Input Error", "Please Enter a Number Between 8 and 16 ")

    except:
        return False

#this function copies the password into clipboard 
def CopytoClipboard():

    test1 = CopyPass()

    if Ouput1.get() != "it's your Password":
        try:

             temp=Ouput1.get()
             test1.Copy(temp)
             mb.showinfo("Successful","Password successfully copied")

        except:
            return False
    else:
        mb.showerror("Copy Error","Password not copied")


#Buttons

ClickButton = tk.Button(Root, command=lambda :Gen(),width=8,height=1 ,text="Generate",bg=Iconsbg, font=("Arial", 12))
ClickButton.place(x=190, y=60)

CopyButton = tk.Button(Root,command=CopytoClipboard,text="Copy",bg=Iconsbg, font=("Arial", 12))
CopyButton.place(x=20,y=165,width=48,height=35)

#Labels

Result = tk.Label(Root, textvariable=Ouput1, font=("Arial", 14),bg="white",fg=Labelsbg)
Result.place(x=20, y=110, height=35, width=255)

InputText = tk.Label(Root, text="Enter a number(8-16)", font=("Arial", 12),bg=Iconsbg,fg="Black")
InputText.place(x=20, y=25)




Root.mainloop()