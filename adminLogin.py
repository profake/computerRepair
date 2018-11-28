from tkinter import *
import tkinter.messagebox
import os
def runfunc(master):
        #Colors and font
        itemFont = "calibri 14 bold"
        bgLight = '#990038'
        bgDark = '#670026'

        photo = PhotoImage(file = "logo.png")
        label = Label(master, image=photo, bg='#340012')
        label.photo = photo
        label.pack()

        def goBack():
            master.destroy()
            os.system('python windowPickerStarter.py')

        #canvas test
        canvas = Canvas(master, width=1280, height=20, bg = "#340012", highlightthickness=0)
        canvas.pack()

        arrow = Button(master, text="←", width = 0, height=0, bg='white', command=goBack)
        arrow.place(x=0, y=0)

        left = Frame(master, width = 807, height = 664, bg = bgLight)
        left.pack()

        title = Label(text="Login", font='Ubuntu 26 bold', bg=bgDark, fg='white')
        title.place(x=110, y=230)

        username = Label(left, text="Username:", font=(itemFont), bg=bgLight, fg='white')
        username.place(x=15, y=140)
        username_entry = Entry(left, width=30)
        username_entry.place(x=120, y=145)

        password = Label(left, text="Password:", font=(itemFont), bg=bgLight, fg='white')
        password.place(x=15, y=180)
        password_entry = Entry(left, show = '*', width=30)
        password_entry.place(x=120, y=185)



        def loginCheck():
            nameVal = username_entry.get().strip()
            passVal = password_entry.get().strip()

            if nameVal == 'admin' and passVal == 'admin':
                master.destroy()
                os.system('python adminLogStarter.py')
            else:
                tkinter.messagebox.showerror("Error", "Incorrect username or password")

        submitButton = Button(left, text="Submit", width=10, height=1, bg="white", command=loginCheck)
        submitButton.place(x=120, y=220)

class initUI:
    def __init__(self, master):
        runfunc(master)
