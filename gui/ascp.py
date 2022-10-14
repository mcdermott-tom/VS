from tkinter import *


root = Tk()


myLabel1 = Label(root, text="ASCP")
myLabel2 = Label(root, text="This is Tom the IT person")
sub = Button(root, text="u know u wanna click me")


sub.grid(row=2, column=8)
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=1,column=0)

root.mainloop()