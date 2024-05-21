# Ask user if he want to use DIC ROLL SIMULATOR
# If said yes, roll die and show number on dic board.
# Ask for another roll and keep doing it, until said otherwise

import random
from matplotlib.pylab import rand, randint

def showDice(n):
    dice_drawing = {
        1: (
            "-------" "\n"
            "|     |" "\n"
            "|  o  |" "\n"
            "|     |" "\n"
            "-------" "\n"
        ),
        2: (
            "-------" "\n"
            "|o    |" "\n"
            "|     |" "\n"
            "|    o|" "\n"
            "-------" "\n"
        ),
        3: (
            "-------" "\n"
            "|o    |" "\n"
            "|  o  |" "\n"
            "|    o|" "\n"
            "-------" "\n"
        ),
        4: (
            "-------" "\n"
            "|o   o|" "\n"
            "|     |" "\n"
            "|o   o|" "\n"
            "-------" "\n"
        ),
        5: (
            "-------" "\n"
            "|o   o|" "\n"
            "|  o  |" "\n"
            "|o   o|" "\n"
            "-------" "\n"
        ),
        6: (
            "-------" "\n"
            "|o   o|" "\n"
            "|o   o|" "\n"
            "|o   o|" "\n"
            "-------" "\n"
        ),
        }
    print(dice_drawing[n][:])




def main():
    print("Welcome to DIC ROLL SIMULATOR!")
    while True:
        answer = input("Would you like to roll the dice? (y/n) ")
        if answer.lower() == "y":
            showDice(randint(1,7))
        elif answer.lower() == "n":
            break
        else:
            print("Please enter y or n")
main()