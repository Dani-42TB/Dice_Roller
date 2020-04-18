import os
from Funcs import *
import time
os.system('cls')

print("\n Welcome to: \n 'Dice Roller 1.2' \n \n")

In = input(" Type 'h' for help, 'c' to close or your dice roll. \n > ")

# Menu loop: This shit was hard to figure out on my own, so it's probably not
# the best solution, but it's my solution. lol. I was actually kinda :| when
# I wrote this and it turned out to be easier than the first few things I tried.
# But hey that's how you learn.
while True:
    if In == 'h' or In == 'H':
        In = help(In)

    elif In == '':
        In = invIn(In)

    elif In == 'c':
        print ('\n Thanks for using! Goodbye!')
        sys.exit()
    else:
        In = checkSyntax(In)
        if In == 'error':
            print ('\n Invalid input...')
            In = input("\n Type 'h' for help, 'c' to close or your dice roll. \n > ")
        else:
            result = dieRoll(In)

            number = str(toInt(In))

            os.system('cls')
            print("\n 'Dice Roller 1.2'")

            print('\n Rolling ' + number + ' ' + In[1] + '...')

            time.sleep(2)

            print('\n Your roll was: ' + str(result))

            In = input("\n Type 'h' for help, 'c' to close or your dice roll. \n > ")
