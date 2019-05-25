from tkinter import *


class Something:
    def __init__(self, stuff):
        frame = Frame(stuff, width=300, height=250)
        frame.pack()

        button1 = Button(frame, text="Click Me!", command=self.message)
        button2 = Button(frame, text="Quit", command=frame.quit)
        button1.pack(side=LEFT)
        button2.pack(side=LEFT)

    def message(self):
        print("That's Wassup")


windows = Tk()

some = Something(windows)

windows.mainloop()