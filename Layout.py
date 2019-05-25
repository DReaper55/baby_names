from tkinter import *

window = Tk()

first = Label(window, text="First", fg='blue', bg='gray')
first.pack()
second = Label(window, text="Second", fg='red', bg='white')
second.pack(fill=X)
third = Label(window, text="Third", fg='green', bg='purple')
third.pack(side=RIGHT, fill=Y)

window.mainloop()