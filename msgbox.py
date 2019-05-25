from tkinter import *
import tkinter.messagebox

windows = Tk()

tkinter.messagebox.showinfo('My Stuff', 'Wasssaaaaaaap!')

quest = tkinter.messagebox.askquestion('Feelings', 'Bro, You Good??')

if quest == 'yes':
    print("Then Go Make Some Money")
else:
    print("Suck it up and then, Go Make Some Money")

windows.mainloop()