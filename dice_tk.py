#!/usr/bin/env python

from tkinter import *
from tkinter import ttk
import re
import random

class App:

    def __init__(self):

        self.root = Tk()
        self.root.geometry('800x600')
        self.root.title('Roll the Dice!')

        # create a menu - to be used and expanded later
        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.filemenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="New", command=self.nullCommand)
        self.filemenu.add_command(label="Open...", command=self.nullCommand)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.root.quit)

        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="About...", command=self.nullCommand)

        self.label = Label(self.root, text='Enter Dice Notation xDy+z').grid(row=0, column=0)

        self.dice_notation = StringVar()
        self.dice =Entry(self.root, textvariable=self.dice_notation, justify=CENTER, width=10).grid(row=0, column=2,
                                                                                                    padx=2, pady=2,
                                                                                                    sticky="e")

        self.results = Message(self.root, text="Results")
        self.results.grid(row=1, column=1, sticky="we")

        self.go_button = Button(self.root, text='Roll the Dice!', command=self.start).grid(row=2, column=1)



        #  Status bar - to be used and expanded later

        #  self.status = Label(self.root, text="-"*80, bd=1, relief=SUNKEN, anchor=W)
        #  self.status.grid(row=3, column=0, columnspan=3)

        self.root.mainloop()

    def nullCommand(self):
        pass

    def parse(self, d):
        dice, dtype_mod = d.split('d')

        dnum = 1
        dtype = 6
        mod = 0

        if dtype_mod:
            if '-' in dtype_mod:
                dtype, mod = dtype_mod.split('-')
                mod = -1 * int(mod)
            elif '+' in dtype_mod:
                dtype, mod = dtype_mod.split('+')
                mod = int(mod)
            else:
                dtype = dtype_mod
        if not dtype: dtype = 6
        if not mod: mod = 0

        return (int(dice), int(dtype), int(mod))

    def roll(self, a, b):
        rolls = []
        t = 0
        r=''

        for i in range(a):
            rolls.append(random.randint(1, b))
            t += int(rolls[i])
            r +=(('Roll number %d is %s, totaling %d \n') % (i + 1, rolls[i], t))
        return (int(t), r)

    def start(self):

        rolls = ''
        modstring = ''
        totalstring = ''

        notation = self.dice_notation.get()

        numbers = self.parse(notation)
        (dice, dtype, mod) = numbers

        (total, rolls) = self.roll(dice, dtype)
        total += mod
        modstring = str(mod)
        totalstring = str(total)
        rolls += str('Mod is ' + modstring + ' making the total ' + totalstring + ' \n')

        self.results.configure(text=rolls)






App()