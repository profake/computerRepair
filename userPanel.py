from tkinter import *
import tkinter.messagebox
import sqlite3
import helpers
import tkinter.ttk as ttk
import tkinter.font as tkFont
import os
#db stuff
conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS log(id INTEGER NOT NULL PRIMARY KEY, client_name TEXT NOT NULL, client_phone TEXT NOT NULL, date_entered TEXT NOT NULL, brand TEXT NOT NULL, model TEXT NOT NULL, problem TEXT NOT NULL, status TEXT NOT NULL, date_done TEXT)")
boxHeaders = ['ID', 'Name', 'Phone', 'Date Added', 'Brand', 'Model', 'Problem',' Status', 'Date Done']
items_list = []

def listPopulator(c_name):
    items_list.clear()
    cur.execute("SELECT * FROM log WHERE client_name = ?", (c_name,))
    for row in cur.fetchall():
        items_list.append(row)

def runfunc(master):
        #Colors and font
        itemFont = "calibri 14 bold"
        bgLight = '#990038'
        bgDark = '#670026'

        #canvas test
        canvas = Canvas(master, width=1280, height=50, bg = "#340012", highlightthickness=0)
        canvas.pack()

        #Left panel
        left = Frame(master, width = 807, height = 664, bg = bgLight)
        left.pack(side = LEFT)

        heading = Label(left, text="Search user info", font='Ubuntu 20 bold', bg=bgLight, fg='white')
        heading.place(x=10, y=30)

        #Left updater panel
        leftUpdater = Frame(master, width = 807, height = 664, bg = bgLight)

        #Right panel
        right = Frame(master, width = 765, height = 664, bg = bgDark)
        right.place(x=520, y=77)
        #right.pack()
        # Title
        title = Label(text="☇Lepot Servicing & Repairs - User", font='Ubuntu 26 bold', bg="#340012", fg='white')
        title.place(x=0, y=0)

        name = Label(left, text="Name:", font=(itemFont), bg=bgLight, fg='white')
        name.place(x=15, y=140)
        name_entry = Entry(left, width=30)
        name_entry.place(x=150, y=145)

        #backButton = Button(leftUpdater, text="Go back", width=10, height=1, bg="white", command=goback)
        #backButton.place(x=415, y=40)

        #--------------------------
        container = ttk.Frame(right)
        container.place(x=15, y=70)
        tree = ttk.Treeview(columns=boxHeaders, show="headings")
        vsb = ttk.Scrollbar(orient="vertical",
                            command=tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
                            command=tree.xview)
        tree.configure(yscrollcommand=vsb.set,
                            xscrollcommand=hsb.set)
        tree.grid(column=0, row=0, sticky='nsew', in_=container)
        #vsb.grid(column=1, row=0, sticky='ns', in_=container)
        #hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        # --------------------------
        for col in boxHeaders:
                tree.heading(col, text=col,
                                  command=lambda c=col: sortby(tree, c, 0))
                # adjust the column's width to the header string
                tree.column(col,  width=tkFont.Font().measure(col.title()) + 30)

        def dbtobox():
            c_name = name_entry.get().strip()
            listPopulator(c_name)

            # clear tree
            for i in tree.get_children():
                tree.delete(i)

            for item in items_list:
                tree.insert('', 'end', values=item)
                # adjust column's width if necessary to fit each value
                #for ix, val in enumerate(item):
                    #col_w = tkFont.Font().measure(val)
                    #if tree.column(boxHeaders[ix], width=None) < col_w:
                        #tree.column(boxHeaders[ix], width=col_w)
        def sortby(tree, col, descending):
            data = [(tree.set(child, col), child) \
                    for child in tree.get_children('')]
            data.sort(reverse=descending)
            for ix, item in enumerate(data):
                tree.move(item[1], '', ix)
            tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

        def logOut():
            master.destroy()
            os.system('python windowPickerStarter.py')

        searchButton = Button(left, text="Search", width=5, height=1, bg="white", command=dbtobox)
        searchButton.place(x=380, y=140)

        logoutButton = Button(right, text="Return", width=10, height=1, bg="white", command=logOut)
        logoutButton.place(x=600, y=10)


class initUI:
    def __init__(self, master):
        runfunc(master)