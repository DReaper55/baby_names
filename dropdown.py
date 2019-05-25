from tkinter import *


class Dropdown:
    def __init__(self):
        frame = Frame(window)
        frame.pack()

    def mainmenu(self):
        first = Menu(window)
        window.config(menu=first)

        firstSub = Menu(first)
        first.add_cascade(label="File", menu=firstSub)
        firstSub.add_command(label="New Project...", command=c.loadProj)
        firstSub.add_command(label="New...", command=c.newProj)
        firstSub.add_separator()
        firstSub.add_command(label="Exit", command=window.quit)

        secSub = Menu(first)
        first.add_cascade(label="Edit", menu=secSub)
        secSub.add_command(label="Copy", command=c.copy)

    def toolbar(self):
        tool = Frame(window, bg="gray")

        button1 = Button(tool, text="Insert Stuffs", command=c.insert)
        button1.pack(side=LEFT, padx=2, pady=2)
        button2 = Button(tool, text="Print Stuffs", command=c.print)
        button2.pack(side=LEFT, padx=2, pady=2)

        tool.pack(side=TOP, fill=X)

    def statusbar(self):
        name = Label(window, text="do something", bd=1, relief=SUNKEN, anchor=W)
        name.pack(side=BOTTOM, fill=X)


class Subfunct(Dropdown):
    def insert(self):
        print("Inserting Stuff")

    def print(self):
        print("Printing stuffs")

    def loadProj(self):
        print("Loading Project")

    def newProj(self):
        print("New Project Loading")

    def copy(self):
        print("Copied")


window = Tk()
window.title("Testing")
window.geometry("300x300")

b = Dropdown()
c = Subfunct()

b.mainmenu()
b.toolbar()
b.statusbar()

window.mainloop()