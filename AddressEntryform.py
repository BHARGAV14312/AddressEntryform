from tkinter import *
root = Tk()

root.title("Address Entry Form")

Input = Frame(root, borderwidth=5, border=2, relief=SUNKEN)
Input.pack(padx=5)

fname = Label(Input,  text = "First Name: ",font="Ariel 11 bold",anchor=E).grid(row = 0, column = 0) 
lname = Label(Input,  text = "Last Name: ",font="Ariel 11 bold", anchor=E).grid(row = 1, column = 0)
age = Label(Input,  text = "Address Line 1: ",font="Ariel 11 bold", anchor=E).grid(row = 2, column = 0)
Gndr = Label(Input,  text = "Address Line 2: ",font="Ariel 11 bold", anchor=E).grid(row = 3, column = 0)
City = Label(Input,  text = "City: ",font="Ariel 11 bold", anchor=E).grid(row = 4, column = 0)
Address = Label(Input,  text = "State/Province: ",font="Ariel 11 bold", anchor=E).grid(row = 5, column = 0)
Uname = Label(Input,  text = "Postal Code: ",font="Ariel 11 bold", anchor=E).grid(row = 6, column = 0)
pwd = Label(Input,  text = "Country: ",font="Ariel 11 bold", anchor=E).grid(row = 7, column = 0)

l1=Entry(Input, width = 50)
l1.grid(row = 0, column = 1)
l2=Entry(Input, width = 50)
l2.grid(row = 1, column = 1)
l3=Entry(Input, width = 50)
l3.grid(row = 2, column = 1)
l4=Entry(Input, width = 50)
l4.grid(row = 3, column = 1)
l5=Entry(Input, width = 50)
l5.grid(row = 4, column = 1)
l6=Entry(Input, width = 50)
l6.grid(row = 5, column = 1)
l7=Entry(Input, width = 50)
l7.grid(row = 6, column = 1)
l8=Entry(Input, width = 50)
l8.grid(row = 7, column = 1)

def Clear():
    global l1, l2, l3, l4, l5, l6, l7, l8
    l1.delete(0, END)
    l2.delete(0, END)
    l3.delete(0, END)
    l4.delete(0, END)
    l5.delete(0, END)
    l6.delete(0, END)
    l7.delete(0, END)
    l8.delete(0, END)

def Show():
    global l1, l2, l3, l4, l5, l6, l7, l8, Output
    fname = l1.get()
    lname = l2.get()
    Output.configure(text=f"Hello {fname} {lname}")

Output = Label(root)
Output.pack(side=BOTTOM)

Clear = Button(root,text="Clear",width=10, command=Clear).pack(side=RIGHT, padx=10, pady=10)
Signup = Button(root,text="Submit",width=10, command=Show).pack(side=RIGHT, pady=10)

root.mainloop()