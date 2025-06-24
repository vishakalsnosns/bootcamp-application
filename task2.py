"""
Plays Higher or Lower with the user for integers between 1 and 100.

Explanation:
- the main loop, GuessingGame(), first gets a validated guess using ValidateInput().
- Then sees if its higher or lower.
- Then repeats until the number has been guessed. 
"""

import random

def ValidateInput():
    try:
        guess = int(input("Guess a number from 1 to 100!"))
        if guess > 100 or guess < 1:
            print("Your number must be between 1 and 100")
        else:
            return guess
    except ValueError:
        print("Input an integer...")

#The main loop of the game.
def GuessingGame(goal):
    guess = None
    
    #Ensure the guess is valid. If a value is returned (not None) it is validated, see GetInput().
    while not guess:
        guess = ValidateInput()

    #Check the ranges respective to the goal value. Recursively call the main loop.
    if guess < goal:
        print(f"{guess} is lower than my number.")
        return GuessingGame(goal)
    elif guess > goal:
        print(f"{guess} is higher than my number.")
        return GuessingGame(goal)
    
    return "You got my number!"

goal = random.randint(1, 100)
print(GuessingGame(goal))