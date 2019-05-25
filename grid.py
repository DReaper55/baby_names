from tkinter import *

window = Tk()

first = Label(window, text="Name")
second = Label(window, text="Password")

entry1 = Entry(window)
entry2 = Entry(window)

first.grid(row=0, sticky=E)
second.grid(row=1)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

check = Checkbutton(window, text="Keep Me Signed In")
check.grid(columnspan=3)

window.mainloop()