'''
                                          This is a guess the number game.
'''

import random

# the var for the guesses taken
takenguess = 0

# the var for username
name = str(input("Enter you're name. "))

# the var for the randomizer (the player is going to guess)
number = random.randint(1, 30)

print("Well, " + name + ", guess a number between 1 and 30.")


# loop for guessing (number)
while takenguess < 6:

    # var for input of you're try to guess the number
    guess = int(input("now try to guess the number!"))

    # adds a turn each time you guess (with +1)
    takenguess = takenguess + 1

    # check's if the input is lower than the number from the randomizer
    if guess < number:
        print("guess higher ")

    # check's if the input is higher than the number from the randomizer
    if guess > number:
        print("guess lower ")

    # check's if the input is equal to the number from the randomizer and if that happens it brakes the loop
    if guess == number:
        break

# check's if the input is equal to the number from the randomizer and printing that you won
if guess == number:
    print("good job " + name + "! you guessed the number in " + str(takenguess) + " guesses!")

# check's if the input is not equal to the number from the randomizer anf printing that you lost
if guess != number:
    print("too bad, the number was " + str(number))
