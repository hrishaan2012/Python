import random
playing = True
number = (random.randint(10,20))
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 10 and 20.")
print("You have to guess a number between 10 and 20.")
while playing:
    guess = int(input("enter your guess:"))
    if guess==number:
        print("Congratulations! You guessed the number correctly.")
    else:
        print("Sorry, that's not correct. Try again.")
