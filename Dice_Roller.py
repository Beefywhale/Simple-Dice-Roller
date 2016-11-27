# Simple Dice Roller

import random

def dice():
    print('')
    prompt = input('What dice would  you like to roll? dice: d4, d6, d8, d10, d12 ')
    print('')
    if prompt.lower() == 'd4':
        d4_random = random.randint(1, 4)
        print('You rolled a d4 and got! ' + str(d4_random))
        exit()

    if prompt.lower() == 'd6':
        d6_random = random.randint(1, 6)
        print('You rolled a d6 and got! ' + str(d6_random))
        exit()

    if prompt.lower() == 'd8':
        d8_random = random.randint(1, 8)
        print('You rolled a d8 and got! ' + str(d8_random))
        exit()

    if prompt.lower() == 'd10':
        d10_random = random.randint(1, 10)
        print('You rolled a d10 and got! ' + str(d10_random))
        exit()

    if prompt.lower() == 'd12':
        d12_random = random.randint(1, 12)
        print('You rolled a d12 and got! ' + str(d12_random))
        exit()

    else:
        print('That dice does not exist!')
        dice()

dice()
