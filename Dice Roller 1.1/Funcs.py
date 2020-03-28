import sys
from random import *
def help(In):
    print ('''
    Help: The format is, # of dice followed by
    die denomination, for example, if you want
    to roll 3 six sided die, you would write
    3d6, 3D6 would also work. :p

    Supported die: d4, d6, d8, d10, d12, d20
    ''')
    In = input("\n Type 'h' for help, 'c' to close or your dice roll. \n > ")
    return In

def invIn(In):
    print ("\n You have to input something...")
    In = input("\n Type 'h' for help, 'c' to close or your dice roll. \n > ")
    return In

def dieRoll(roll):
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


    if check[0] in numbers:
        if check[0] == '':
            if check[1] in diceTypes:
                return check
            else:
                return 'error'
        if check[1] in diceTypes:
            return check
    else:
        return 'error'
