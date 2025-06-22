import random

def GetInput():
    try:
        guess = int(input("Guess a number from 1 to 100!"))
        if guess > 100 or guess < 1:
            print("Your number must be between 1 and 100")
        else:
            return guess
    except ValueError:
        print("Input an integer...")

def GuessingGame(goal):
    guess = None
    while not guess:
        guess = GetInput()

    if guess < goal:
        print(f"{guess} is lower than my number.")
        return GuessingGame(goal)
    elif guess > goal:
        print(f"{guess} is higher than my number.")
        return GuessingGame(goal)
    
    return "You got my number!"

print(GuessingGame(random.randint(1, 100)))