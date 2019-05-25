from tkinter import *

windows = Tk()


def left(event):
    print("Left")


def right(event):
    print("Right")


frame = Frame(windows, width=600, height=400)
frame.bind("<Button-1>", left)
frame.bind("<Button-3>", right)

frame.pack()

windows.mainloop()