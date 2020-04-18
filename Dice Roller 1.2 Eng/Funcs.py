import sys
import os
from random import *

# This file is what it is, I guess I might be able to do this another way, with
# classes maybe (??) But for now, I'm starting out and this works, and I can
# Understand how.

def toInt(In):
    '''
    this is so if you just write for example d20. it turns the '' in the Input
    list, into a 1, to roll a single die. I could've done it another way maybe,
    but getting the 'menu' with help and invalid input to work by my own was tireing,
    so this just wokrs.
    '''
    if In[0] == '':
        return str(1)
    else:
        return In[0]

def help(In):
    '''
    Called when In is 'h' or 'H'
    ----------------
    prints: Information on what the program expects as Input.
    ----------------
    Input: Asks for a new input.
    ----------------
    returns input In.
    '''
    os.system('cls')
    print ('''
                        Help

        To roll a die  you have to write the # of die
    to roll followed by die denomination, for example,
    if  you want  to roll  3 six sided die,  you would
    write '3d6' (No air quotes), '3D6' would also work,
    for single dice, 1d6 or d6 would both work.

    Supported denominations: d4, d6, d8, d10, d12, d20
    ''')
    In = input("\n Type 'h' for help, 'c' to close or your dice roll. \n > ")
    return In

def invIn(In):
    '''
    Called when '' is entered as input.
    Takes 1 argument In.
    --------------------
    prints error message
    ---------------------
    returns new input : In
    '''
    print ("\n You have to input something...")
    In = input("\n Type 'h' for help, 'c' to close or your dice roll. \n > ")
    return In

#This function is called when you get the right format, to initiate the roll.
def dieRoll(roll):
    '''
    Takes one input List 'roll'
    ------------------
     Your roll input (now: In) after being processed by checkSyntax()
    ------------------
    returns an int :
        your result
    '''
    if roll[0] == '':
        numberOfDie = 1
    else:
        numberOfDie = int(roll[0])
    if roll[1] == 'd4' or roll[1] == 'D4':
        return rollD4(numberOfDie)
    elif roll[1] == 'd6' or roll[1] == 'D6':
        return rollD6(numberOfDie)
    elif roll[1] == 'd8' or roll[1] == 'D8':
        return rollD8(numberOfDie)
    elif roll[1] == 'd10' or roll[1] == 'D10':
        return rollD10(numberOfDie)
    elif roll[1] == 'd12' or roll[1] == 'D12':
        return rollD12(numberOfDie)
    elif roll[1] == 'd20' or roll[1] == 'D20':
        return rollD20(numberOfDie)

# This are all the functions for the different die.

def rollD4(numberOfDie):
    '''
    Takes one input: numberOfDice
    --------------------------
    returns a d4 die roll, times the number of die.
    '''
    if numberOfDie == 1:
        return randint(1,4)
    else:
        return (randint(1,4) + rollD4(numberOfDie-1))

def rollD6(numberOfDie):
    '''
    Takes one input: numberOfDice
    --------------------------
    returns a d6 die roll, times the number of die.
    '''
    if numberOfDie == 1:
        return randint(1,6)
    else:
        return (randint(1,6) + rollD6(numberOfDie-1))

def rollD8(numberOfDie):
    '''
    Takes one input: numberOfDice
    --------------------------
    returns a d8 die roll and adds any aditional rolls.
    '''
    if numberOfDie == 1:
        return randint(1,8)
    else:
        return (randint(1,8) + rollD6(numberOfDie-1))

def rollD10(numberOfDie):
    '''
    Takes one input: numberOfDice
    --------------------------
    returns a d10 die roll, times the number of die.
    '''
    if numberOfDie == 1:
        return randint(1,10)
    else:
        return (randint(1,10) + rollD6(numberOfDie-1))

def rollD12(numberOfDie):
    '''
    Takes one input: numberOfDice
    --------------------------
    returns a d12 die roll, times the number of die.
    '''
    if numberOfDie == 1:
        return randint(1,12)
    else:
        return (randint(1,12) + rollD6(numberOfDie-1))

def rollD20(numberOfDie):
    '''
    Takes one input: numberOfDice
    --------------------------
    returns a d20 die roll, times the number of die.
    '''
    if numberOfDie == 1:
        return randint(1,20)
    else:
        return (randint(1,20

        ) + rollD6(numberOfDie-1))

def checkSyntax(In):
    """
    Takes two inputs >

    In: Input from end User
        diceTypes: the dice types.
    -----------
    Returns

        syntax: A list syntax = [Number of die to roll, type of dice]
    -----------

    """
    diceTypes = ['d4', 'd6', 'd8', 'd10', 'd12', 'd20',
     'D4', 'D6', 'D8', 'D10', 'D12', 'D20']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '']
    numberOfDice = ''
    diceType = ''
    for ch in range(len(In)):
        if In[ch] in numbers:
            numberOfDice += In[ch]
        elif In[ch] == 'd' or In[ch] == 'D':
            diceType = In[ch:len(In)+1]
            break
        else:
            break

    check = [numberOfDice, diceType]

    if check[0] == '':
        check[0] = '1'
    try:
        check[0] = int(check[0])
    except:
        return 'error'
    if check[1] in diceTypes:
        return check
    else:
        return 'error'
