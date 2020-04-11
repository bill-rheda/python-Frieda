'''A program that request two numbers from the user and prints out the sum or difference or product 
or dividend or remainder depending on what the user request'''

import sys

guess1 = int(input("Enter a number "))
guess2 = int(input("Enter another number "))
answer = int(input("Which operation do you wish to perform?\n Enter\n 1 for Addition\n 2 for subtraction\n\
 3 for multiplication\n 4 for division\n 5 for modulo\n"))

def calculator():

    if answer == 1:
        sum = guess1 +  guess2
        print("The sum of " + str(guess1) + " and " + str(guess2) + " is " + str(sum))

    elif answer == 2:
        difference = guess1 -guess2
        print("The difference between " + str(guess1) + " and " + str(guess2) + " is " + str(difference))

    elif answer == 3:
        product = guess1 * guess2
        print("The product of " + str(guess1) + " and " + str(guess2)  + " is " + str(product))

    elif answer == 4:
        dividend = guess1 // guess2
        print("The dividend of " + str(guess1) + " and " + str(guess2) + " is "  + str(dividend))

    elif answer == 5:
        remainder = guess1 % guess2
        print("The remainder of the division between " + str(guess1) + " and " + str(guess2) + " is " + str(remainder))

    else:
        print("The answer you entered is not valid! Please follow the instructions")

calculator()