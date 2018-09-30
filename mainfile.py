from tkinter import *
import initui

#tk main window
root = Tk()
x = initui.initUI(root) #it's in a different file because its cluttered :@

#config root (main) window
root.geometry("1280x768")
root.configure(background='orange')
root.resizable(False, False)
root.wm_title("Lepot Servicing & Repairs")
#Run program

root.mainloop()
#-----------------
