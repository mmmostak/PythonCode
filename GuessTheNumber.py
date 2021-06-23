# This is a guess the number game.
import random

name = input('Hello! What is your name? ')
print('Well, ' + name + ', I\'m thinking of a number between 1 and 15')
secretNumber = random.randint(1, 15)

for guessesTaken in range(1, 6):
    guess = int(input('Take a guess: '))

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for correct guess!

if guess == secretNumber:
    print('WELL DONE, ' + name + '! You guessed the correct number in ' + str(guessesTaken) + ' guesses.')
else:
    print('Oh NO! The number I was thinking of was ' + str(secretNumber) + '.')
