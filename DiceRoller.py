# Simple Dice Roller

import random

def dice():
    print('')
    prompt = input('What dice would  you like to roll? ')
    print('')
    if prompt.lower().startswith('d'):
        dice_random = random.randint(1, int(prompt.lower().strip('d')))
        print('You rolled a ' + prompt + ' and got: ' + str(dice_random))

    else:
        print('That dice does not exist!')
        dice()

dice()
