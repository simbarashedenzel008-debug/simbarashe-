import random

number = random.randrange(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number (1-100): "))
    attempts += 1

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("Correct!")
        print("Attempts:", attempts)
        break
