#A program that inputs two numbers and checks whether one is a multiple of the other
import sys
guess1 = int(input ("Enter a number "))
guess2 = int(input("Enter another number "))

def Multiplicator():
    if guess1 >= guess2:
        if guess1 % guess2 is 0:
            print (str(guess1) + " is a mutiple of " + str(guess2))
        else:
            print(str(guess1) + " is greater than " + str(guess2) + " but is not a multiple of " + str(guess2))
    else:
        print(str(guess1) + " is less than " + str(guess2) + " thus not a multiple of " + str(guess2))

Multiplicator()