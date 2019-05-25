from tkinter import *

window = Tk()

topSide = Frame(window)
topSide.pack()
bottomSide = Frame(window)
bottomSide.pack(side=BOTTOM)

Button1 = Button(topSide, text="First", fg="blue", bg="red")
Button2 = Button(topSide, text="Second", fg="red")
Button3 = Button(topSide, text="Third", fg="grey")
Button4 = Button(bottomSide, text="Fourth", fg="green")

Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
Button3.pack(side=LEFT)
Button4.pack()


window.mainloop()