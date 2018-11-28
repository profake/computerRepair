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

def listPopulator():
    items_list.clear()
    cur.execute("SELECT * FROM log")
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

        #Left updater panel
        leftUpdater = Frame(master, width = 807, height = 664, bg = bgLight)

        #Right panel
        right = Frame(master, width = 765, height = 664, bg = bgDark)
        right.place(x=520, y=77)
        #right.pack()
        # Title
        title = Label(text="☇Lepot Servicing & Repairs", font='Ubuntu 26 bold', bg="#340012", fg='white')
        title.place(x=0, y=0)

        # Add to log
        heading = Label(left, text="Add to log", font='Ubuntu 20 bold', bg=bgLight, fg='white')
        heading.place(x=10, y=30)

        # Log
        headingR = Label(right, text="Log", font='Ubuntu 20 bold', bg="#340012", fg="white")
        headingR.place(x=30, y=0)

        id = Label(left, text="ID:", font=(itemFont), bg=bgLight, fg='white')
        id.place(x=15, y=100)
        id_entry = Entry(left, width=30)
        id_entry.place(x=250, y=105)

        name = Label(left, text="Client Name:", font=(itemFont), bg=bgLight, fg='white')
        name.place(x=15, y=140)
        name_entry = Entry(left, width=30)
        name_entry.place(x=250, y=145)

        phone = Label(left, text="Client Phone:", font=(itemFont), bg=bgLight, fg='white')
        phone.place(x=15, y=180)
        phone_entry = Entry(left, width=30)
        phone_entry.place(x=250, y=185)

        dateAdd = Label(left, text="Date of Addition:", font=(itemFont), bg=bgLight, fg='white')
        dateAdd.place(x=15, y=220)
        dateAdd_entry = Entry(left, width=30)
        dateAdd_entry.place(x=250, y=225)

        brand = Label(left, text="Brand:", font=(itemFont), bg=bgLight, fg='white')
        brand.place(x=15, y=260)
        brand_entry = Entry(left, width=30)
        brand_entry.place(x=250, y=265)

        model = Label(left, text="Model:", font=(itemFont), bg=bgLight, fg='white')
        model.place(x=15, y=300)
        model_entry = Entry(left, width=30)
        model_entry.place(x=250, y=305)

        problem = Label(left, text="Problem:", font=(itemFont), bg=bgLight, fg='white')
        problem.place(x=15, y=340)
        problem_entry = Entry(left, width=30)
        problem_entry.place(x=250, y=345)

        # status = Label(left, text = "Status:", font=(itemFont), bg=bgLight, fg = 'white')
        # status.place(x = 15, y = 380)
        # status_entry = Entry(left, width=30)
        # status_entry.place(x=250, y=385)

        # dateDone = Label(left, text = "Date done:", font=(itemFont), bg=bgLight)
        # dateDone.place(x = 15, y = 420)
        # dateDone_entry = Entry(left, width=30)
        # dateDone_entry.place(x=250, y=425)


        def updater_panel():
            #Remove left panel
            left.pack_forget()

            #Add leftupdater to screen
            leftUpdater.pack(side = LEFT)
            headingUpd = Label(leftUpdater, text="Update log", font='Ubuntu 20 bold', bg=bgLight, fg='white')
            headingUpd.place(x=10, y=30)

            id = Label(leftUpdater, text="Enter ID to update:", font=(itemFont), bg=bgLight, fg='white')
            id.place(x=15, y=100)
            id_entry = Entry(leftUpdater, width=30)
            id_entry.place(x=250, y=105)

            # search button func
            def search():
                idVal = id_entry.get().strip()
                def update():
                    idVal = id_entry.get().strip()
                    nameVal = name_entry.get().strip()
                    phoneVal = Uphone_entry.get().strip()
                    dateAddVal = UdateAdd_entry.get().strip()
                    brandVal = Ubrand_entry.get().strip()
                    modelVal = Umodel_entry.get().strip()
                    problemVal = Uproblem_entry.get().strip()
                    statusVal = Ustatus_entry.get().strip()
                    dateDoneVal = UdateDone_entry.get().strip()
                    if idVal == '' or nameVal == '' or phoneVal == '' or dateAddVal == '' or brandVal == '' or modelVal == '' or problemVal == '' or statusVal == '' or dateDoneVal == '':
                        tkinter.messagebox.showerror("Warning", "Please fill up all the entries")
                    else:
                        if not helpers.RepresentsInt(idVal):
                            tkinter.messagebox.showerror("Warning", "Please enter an integer value as ID")
                        else:
                            try:
                                cur.execute("UPDATE log SET id = ?, client_name = ?, client_phone = ?, date_entered = ?, brand = ?, model = ?, problem = ?, status = ?, date_done = ? WHERE id = ?",
                                            (idVal, nameVal, phoneVal, dateAddVal, brandVal, modelVal, problemVal, statusVal, dateDoneVal, idVal))
                                conn.commit()
                                dbtobox()
                                tkinter.messagebox.showinfo("Message",
                                                            "Entry updated successfully for ID: " + idVal + " " + brandVal + " " + modelVal)
                            except sqlite3.IntegrityError as e:
                                tkinter.messagebox.showerror("Error", "ID already in use")
                def delete():
                    delVal = int(idVal)
                    result = tkinter.messagebox.askquestion("Confirmation", "Are you sure you want to delete entry with ID: %d?" %delVal)
                    if result == 'yes':
                        cur.execute("DELETE FROM log WHERE id = ?", (delVal,))
                        conn.commit()
                        dbtobox()
                        tkinter.messagebox.showinfo("Information", "Entry %d was deleted sucessfully." %delVal)

                if idVal == "":
                    tkinter.messagebox.showerror("Error", "Please enter an ID")
                elif not helpers.RepresentsInt(idVal):
                    tkinter.messagebox.showerror("Error", "Please enter a valid integer ID")
                else:
                    idVal = int(idVal)
                    cur.execute("SELECT * FROM log WHERE id = ?", (idVal,))
                    data = cur.fetchall()
                    #if not means empty
                    if not data:
                        tkinter.messagebox.showerror("Error", "No such ID found")
                    else:

                        name = Label(leftUpdater, text="Client Name:", font=(itemFont), bg=bgLight, fg='white')
                        name.place(x=15, y=140)
                        name_entry = Entry(leftUpdater, width=30)
                        name_entry.place(x=250, y=145)
                        name_entry.insert(0, data[0][1])

                        Uphone = Label(leftUpdater, text="Client Phone:", font=(itemFont), bg=bgLight, fg='white')
                        Uphone.place(x=15, y=180)
                        Uphone_entry = Entry(leftUpdater, width=30)
                        Uphone_entry.place(x=250, y=185)
                        Uphone_entry.insert(0, data[0][2])

                        UdateAdd = Label(leftUpdater, text="Date of Addition:", font=(itemFont), bg=bgLight, fg='white')
                        UdateAdd.place(x=15, y=220)
                        UdateAdd_entry = Entry(leftUpdater, width=30)
                        UdateAdd_entry.place(x=250, y=225)
                        UdateAdd_entry.insert(0, data[0][3])

                        Ubrand = Label(leftUpdater, text="Brand:", font=(itemFont), bg=bgLight, fg='white')
                        Ubrand.place(x=15, y=260)
                        Ubrand_entry = Entry(leftUpdater, width=30)
                        Ubrand_entry.place(x=250, y=265)
                        Ubrand_entry.insert(0, data[0][4])

                        Umodel = Label(leftUpdater, text="Model:", font=(itemFont), bg=bgLight, fg='white')
                        Umodel.place(x=15, y=300)
                        Umodel_entry = Entry(leftUpdater, width=30)
                        Umodel_entry.place(x=250, y=305)
                        Umodel_entry.insert(0, data[0][5])

                        Uproblem = Label(leftUpdater, text="Problem:", font=(itemFont), bg=bgLight, fg='white')
                        Uproblem.place(x=15, y=340)
                        Uproblem_entry = Entry(leftUpdater, width=30)
                        Uproblem_entry.place(x=250, y=345)
                        Uproblem_entry.insert(0, data[0][6])

                        Ustatus = Label(leftUpdater, text = "Status:", font=(itemFont), bg=bgLight, fg = 'white')
                        Ustatus.place(x = 15, y = 380)
                        Ustatus_entry = Entry(leftUpdater, width=30)
                        Ustatus_entry.place(x=250, y=385)
                        Ustatus_entry.insert(0, data[0][7])

                        UdateDone = Label(leftUpdater, text = "Date done:", font=(itemFont), bg=bgLight, fg='white')
                        UdateDone.place(x = 15, y = 420)
                        UdateDone_entry = Entry(leftUpdater, width=30)
                        UdateDone_entry.place(x=250, y=425)
                        UdateDone_entry.insert(0, data[0][8])

                        updateButton = Button(leftUpdater, text="Update Entry", width=10, height=1, bg="white", command=update)
                        deleteButton = Button(leftUpdater, text="Delete Entry", width=10, height=1, bg="white", command=delete)
                        updateButton.place(x=250, y=460)
                        deleteButton.place(x=350, y=460)
            #Back to entry panel
            def goback():
                leftUpdater.pack_forget()
                left.pack(side=LEFT)

            backButton = Button(leftUpdater, text="Go back", width=10, height=1, bg="white", command=goback)
            backButton.place(x=415, y=40)
            searchButton = Button(leftUpdater, text = "Search", width = 5, height = 1, bg = "white", command = search)
            searchButton.place(x=450, y=102)

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
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        # --------------------------
        for col in boxHeaders:
                tree.heading(col, text=col,
                                  command=lambda c=col: sortby(tree, c, 0))
                # adjust the column's width to the header string
                tree.column(col,
                                 width=tkFont.Font().measure(col.title()))
        def dbtobox():
            listPopulator()

            # clear tree
            for i in tree.get_children():
                tree.delete(i)

            for item in items_list:
                tree.insert('', 'end', values=item)
                # adjust column's width if necessary to fit each value
                for ix, val in enumerate(item):
                    col_w = tkFont.Font().measure(val)
                    if tree.column(boxHeaders[ix], width=None) < col_w:
                        tree.column(boxHeaders[ix], width=col_w)
        dbtobox()

        #Scrolling box
        #box = Listbox(right, width=70, height=35)
        #box.place(x=15, y=70)

        def sortby(tree, col, descending):
            data = [(tree.set(child, col), child) \
                    for child in tree.get_children('')]
            data.sort(reverse=descending)
            for ix, item in enumerate(data):
                tree.move(item[1], '', ix)
            tree.heading(col, command=lambda col=col: sortby(tree, col, int(not descending)))

        def clearentries():
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            phone_entry.delete(0, END)
            dateAdd_entry.delete(0, END)
            brand_entry.delete(0, END)
            model_entry.delete(0, END)
            problem_entry.delete(0, END)

        def submit():
            idVal = id_entry.get().strip()
            nameVal = name_entry.get().strip()
            phoneVal = phone_entry.get().strip()
            dateAddVal = dateAdd_entry.get().strip()
            brandVal = brand_entry.get().strip()
            modelVal = model_entry.get().strip()
            problemVal = problem_entry.get().strip()
            #statusVal = status_entry.get()
            if idVal == '' or nameVal == '' or phoneVal == '' or dateAddVal == '' or brandVal == '' or modelVal == '' or problemVal == '':
                tkinter.messagebox.showerror("Warning", "Please fill up all the entries")
            else:
                if not helpers.RepresentsInt(idVal):
                    tkinter.messagebox.showerror("Warning", "Please enter an integer value as ID")
                else:
                    try:
                        cur.execute("INSERT INTO log VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (idVal, nameVal, phoneVal, dateAddVal, brandVal, modelVal, problemVal, 'Not Done', ''))
                        conn.commit()
                        dbtobox()
                        tkinter.messagebox.showinfo("Message", "Entry added successfully for " + brandVal + " " + modelVal)
                        clearentries()
                    except sqlite3.IntegrityError as e:
                        tkinter.messagebox.showerror("Error", "ID already in use")
        def logOut():
            master.destroy()
            os.system('python windowPickerStarter.py')

        submitButton = Button(left, text = "Add Entry", width = 10, height = 1, bg = "white", command = submit)
        clearButton = Button(left, text = "Clear", width = 5, height = 1, bg = "white", command = clearentries)
        updateButton = Button(left, text="Update", width = 10, height= 2, bg = "white", command = updater_panel)
        logoutButton = Button(right, text="Log Out", width=10, height=1, bg="white", command=logOut)
        submitButton.place (x=315, y=400)
        clearButton.place (x=265, y=400)
        updateButton.place(x=290, y=450)
        logoutButton.place(x=600, y=10)



class initUI:
    def __init__(self, master):
        runfunc(master)
