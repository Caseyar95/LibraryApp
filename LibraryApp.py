from tkinter import *
from backend import Database

database = Database()

def get_selected(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        eTitle.delete(0, END)
        eTitle.insert(END, selected_tuple[1])
        eAuthor.delete(0, END)
        eAuthor.insert(END, selected_tuple[2])
        eYear.delete(0, END)
        eYear.insert(END, selected_tuple[3])
        eRead.delete(0, END)
        eRead.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list1.delete(0, END)
    for row in database.viewAll():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), Read_text.get()):
        list1.insert(END, row)

def add_command():
    database.insert(title_text.get(), author_text.get(), year_text.get(), Read_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), Read_text.get()))

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), Read_text.get())
    view_command()


window = Tk()

window.wm_title("Library")

lTitle = Label(window, text="Title")
lTitle.grid(row=0, column=0)

lAuthor = Label(window, text="Author")
lAuthor.grid(row=0, column=2)

lYear = Label(window, text="Year")
lYear.grid(row=1, column=0)

lRead = Label(window, text="Read")
lRead.grid(row=1, column=2)

title_text = StringVar()
eTitle = Entry(window, textvariable=title_text)
eTitle.grid(row=0, column=1)

author_text = StringVar()
eAuthor = Entry(window, textvariable=author_text)
eAuthor.grid(row=0, column=3)

year_text = StringVar()
eYear = Entry(window, textvariable=year_text)
eYear.grid(row=1, column=1)

Read_text = StringVar()
eRead = Entry(window, textvariable=Read_text)
eRead.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=50)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sbList = Scrollbar(window)
sbList.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sbList.set)
sbList.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected)

bVa = Button(window, text="View all", width=12, command=view_command)
bVa.grid(row=2, column=3)

bSe = Button(window, text="Search entry", width=12, command=search_command)
bSe.grid(row=3, column=3)

bAe = Button(window, text="Add entry", width=12, command=add_command)
bAe.grid(row=4, column=3)

bUp = Button(window, text="Update", width=12, command=update_command)
bUp.grid(row=5, column=3)

bDel = Button(window, text="Delete", width=12, command=delete_command)
bDel.grid(row=6, column=3)

bC = Button(window, text="Close", width=12, command=window.destroy)
bC.grid(row=7, column=3)


window.mainloop()
