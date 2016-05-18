#!/usr/bin/env python

from tkinter import *


class TwoButtons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Something", command=self.printSomething)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printSomething(self):
        print('Hot damn!  This actually worked!')

def doNothing():
    print("Okay, okay, I won't")

root = Tk()

buttons = TwoButtons(root)

menu1 = Menu(root)
root.config(menu=menu1)

subMenu = Menu(menu1)
menu1.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Does nothing", command=doNothing)
subMenu.add_command(label="also does nothing", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="does not Exit", command=doNothing)

editMenu = Menu(menu1)
menu1.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="REALLY does nothing!", command=doNothing)

toolbar = Frame(root, bg="blue")

insertButt = Button(toolbar, text="Insert Butt", command=doNothing)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text="Print Butt", command=doNothing)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
