from tkinter import *
from tkinter import Tk
root= Tk()
root.geometry("500x300")
Label(root, text= "Python Registration Form",font="ar 15 bold").grid(row=0,column=3)
name =Label(root, text ='Name')
phone =Label(root, text ='Phone')
gender =Label(root, text ='Gender')
number =Label(root, text ='Address')

def getvals():
    print("Accepted")
    
name.grid(row=1,column =2)
phone.grid(row=2,column =2)
gender.grid(row=3,column =2)
number.grid(row=4,column =2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
numbervalue = StringVar
checkvalue=IntVar

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
numberentry = Entry(root, textvariable=numbervalue)


nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
numberentry.grid(row=4,column=3)

checkbtn =Checkbutton(text="Remember me",variable=checkvalue)
checkbtn.grid(row=6,column=3)

#submit
Button(text="Submit",command=getvals).grid(row=7,column=3)

root.mainloop()