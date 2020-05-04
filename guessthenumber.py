import random

i = random.randint(0, 21)

def number():
    p = input('Choose a number 0 - 20: ')

    if p.isdigit() == True:
        p = int(p)

        if p > 20 or p < 0:
            print('The number you have chosen is not in the boundaries.')
            number()

        if p > i:
            print('The number that you have chosen is higher than the number.')
            number()

        elif p < i:
            print('The number that you have chosen is lower than the number.')
            number()

        else:
            print('You have chosen the number. Congrats!')

    elif len(p) == 0:
        print('Write a number.')
        number()

    else:
        print('You can only write a number.')
        number()
o = number()
