import os
from Funcs import *
import time
os.system('cls')

def roll(In, syntax):
    pass


print('Welcome to dice roller - Alpha 1.1 \n \n')

In = input("Type 'h' for help, 'c' to close or your dice roll. \n > ")

while True:
    if In == 'h' or In == 'H':
        In = help(In)

    elif In == '':
        In = invIn(In)

    elif In == 'c':
        print ('Goodbye!')
        sys.exit()
    else:
        In = checkSyntax(In)
        if In == 'error':
            print ('\n Invalid input...')
            In = input("\n Type 'h' for help, 'c' to close or your dice roll. \n > ")
        else:
            break

result = dieRoll(In)
if In[0] == '':
    number = str(1)
else:
    number = In[0]

print('Rolling ' + number + ' ' + In[1] + '...')

time.sleep(2)

print('Your roll was: ' + str(result) + '!')
