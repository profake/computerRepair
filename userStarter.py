from tkinter import *
import userPanel

#tk main window
userStart = Tk()
x = userPanel.initUI(userStart)

#config root (main) window
userStart.geometry("1280x768")
userStart.configure(background='#340012')
userStart.resizable(False, False)
userStart.wm_title("Lepot Servicing & Repairs - User")

#Run program
userStart.mainloop()
#-----------------
