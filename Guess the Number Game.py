# Guess the Number Game
import random

secret_number = random.randint(1, 10)

attempts = 0

print("Welcome to Guess the Number Game!")
print("I have choosen a number between 1 to 10.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try gain.")

    elif guess > secret_number:
        print("Too High! Try gain.")
    
    else:
        print(f"Conratulations! You guessed it in {attempts} attempts.")
        break
