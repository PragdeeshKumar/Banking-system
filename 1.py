from tkinter import *
import os
from PIL import ImageTk, Image

#main screen
master = Tk()
master.title('Banking app')

#functions
def finish_reg():
      Name = temp_Name.get()
      Age = temp_Age.get()
      Gender = temp_Gender.get()
      Password = temp_Password.get()
      all_accounts = os.listdir()
      print(all_accounts)


def register():
    #Vars
    global temp_Name
    global temp_Age
    global temp_Gender
    global temp_Password
    temp_Name=StringVar
    temp_Age=StringVar
    temp_Gender=StringVar
    temp_Password=StringVar

    #Register screen
    register_screen = Toplevel(master)
    register_screen.title('Register')

    #Labels
    Label(register_screen, text='Pls enter your details to register', font=('tahoma, 12')).grid(row=0, sticky=N, pady=10)
    Label(register_screen, text='Name', font=('tahoma, 12')).grid(row=1, sticky=W)
    Label(register_screen, text='Age', font=('tahoma, 12')).grid(row=2, sticky=W)
    Label(register_screen, text='Gender', font=('tahoma, 12')).grid(row=3, sticky=W)
    Label(register_screen, text='Password', font=('tahoma, 12')).grid(row=4, sticky=W)

    #Entries
    Entry(register_screen, textvariable=temp_Name).grid(row=1, column=0)
    Entry(register_screen, textvariable=temp_Age).grid(row=2, column=0)
    Entry(register_screen, textvariable=temp_Gender).grid(row=3, column=0)
    Entry(register_screen, textvariable=temp_Password, show="*").grid(row=4, column=0)

    #Buttons
    Button(register_screen, text='Register', command = finish_reg, font = ('tahoma,12')).grid(row=5, sticky=N, pady=10)

def login():
    print('This is our login page')



#image import
img = Image.open('img.jpg')
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

#Labels
Label(master, text='Costum banking beta', font=('tahoma', 14)).grid(row=0, sticky=N, pady=10)
Label(master, text='Most secured bank which is used probably', font=('tahoma', 12)).grid(row=1, sticky=W)
Label(master, image = img).grid(row=2, sticky=N, pady=15)

#Buttons
Button(master, text='Register', font=('tahoma, 12') ,width=20, command=register).grid(row=3, sticky=N)
Button(master, text='Login', font=('tahoma, 12') ,width=20, command=login).grid(row=4, sticky=N, pady=5)

master.mainloop()

