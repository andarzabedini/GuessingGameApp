# This example shows how to use if-else statement and random number generator
# Users set the max number for the number guessing game
# Users have 3 chances to pick the correct number
# Each missed pick will reset the range for the next pick
#
# Python Syntax and Methods: if-else, input(), str(), int(), random
#
# Postcondition: a message to show whether user got the correct pick within 3 tries

import random
print("Welcome to number Guessing Game App...")
maxNumber =int(input("Enter the maximum number for your game:"))
# randomly generating a number from 0 to maxNumber
targetNumber = random.randrange(0, maxNumber)
guess1 = int(input("Now, pick a number in between 0 and " + str(maxNumber) + ":"))
style = "You miss!! Try again and pick a number in between {0} and {1}:"
rightMessage = "Good job!! You got it right"
missMessage = "Sorry, you did not guess the correct number {0} within 3 tries!"

if guess1 == targetNumber: # correct pick at the first try
    print(rightMessage)
elif guess1 > targetNumber: # the picked number is greater than the target
    # Get the second pick in between 0 and the first picked number
    guess2 = int(input(style.format(0, guess1)))
    if guess2 == targetNumber: # correct pick at the second try
        print(rightMessage)
    elif guess2 > targetNumber: # the picked number is greater than the target
        # Get the third pick in between 0 and the second picked number
        guess3 = int(input(style.format(0, guess2)))
        if guess3 == targetNumber: # correct pick at the third try
            print(rightMessage)
        else: # Miss all 3 tries
            print(missMessage.format(targetNumber))
    elif guess2 < targetNumber: # the picked number is smaller than the target
        # Get the third pick in between the second picked number and the first picked number
        guess3 = int(input(style.format(guess2, guess1)))
        if guess3 == targetNumber:  # correct pick at the third try
            print(rightMessage)
        else: # Miss all 3 tries
            print(missMessage.format(targetNumber))
elif guess1 < targetNumber: # the picked number is smaller than the target
    # Get the second pick in between the first picked number and max number
    guess2 = int(input(style.format(guess1, maxNumber)))
    if guess2 == targetNumber: # correct pick at the second try
        print(rightMessage)
    elif guess2 > targetNumber:# the picked number is greater than the target
        # Get the third pick in between the second picked number and the first picked number
        guess3 = int(input(style.format(guess1, guess2)))
        if guess3 == targetNumber: # correct pick at the third try
            print(rightMessage)
        else: # Miss all 3 tries
            print(missMessage.format(targetNumber))
    elif guess2 < targetNumber: # the picked number is smaller than the target
        # Get the third pick in between the second picked number and max number
        guess3 = int(input(style.format(guess2, maxNumber)))
        if guess3 == targetNumber: # correct pick at the third try
            print(rightMessage)
        else: # Miss all 3 tries
            print(missMessage.format(targetNumber))