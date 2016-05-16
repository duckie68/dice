#!/usr/bin/env python

import re
import random

def parse(d):
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

def roll(a, b):
    rolls = []
    t = 0
    
    for i in range(a):
        rolls.append(random.randint(1,b))
        t += int(rolls[i])
        print(('Roll number %d is %s, totaling %d') % (i+1, rolls[i], t))
    return(int(t))

random.seed()
notation = ""

while True:
    notation = raw_input('Please input dice notation or q to quit: ')
    
    if notation == "q":
        raise SystemExit
    else:
        print(notation)
        
        numbers = parse(notation)
        (dice, dtype, mod) = numbers
        
        total = roll(dice, dtype)
        total += mod
        
        print('Your total is %d' % total)

