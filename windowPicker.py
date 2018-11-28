from tkinter import *
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

        #canvas test
        canvas = Canvas(master, width=1280, height=20, bg = "#340012", highlightthickness=0)
        canvas.pack()

        left = Frame(master, width = 807, height = 664, bg = bgLight)
        left.pack()

        title = Label(text="Start", font='Ubuntu 26 bold', bg=bgLight, fg='white')
        title.place(x=5, y=230)

        iAmA = Label(text="I am a...", font='Ubuntu 20 bold', bg=bgLight, fg='white')
        iAmA.place(x=35, y=350)

        def adminPanel():
            master.destroy()
            os.system('python adminLoginWindow.py')
        def userPanel():
            master.destroy()
            os.system('python userStarter.py')

        userButton = Button(left, text="User", width=10, height=1, bg="white", command=userPanel)
        userButton.place(x=60, y=220)

        adminButton = Button(left, text="Admin", width=10, height=1, bg="white", command=adminPanel)
        adminButton.place(x=180, y=220)

class initUI:
    def __init__(self, master):
        runfunc(master)
