import random
import time

x=random.randint(1,100)

def intro():
    print("What is your name?")
    global x
    global name
    name=input()
    print("Hello, "+name+"! Welcome to the Number Guessing Game!")
    if(x%2==0):
       print("The number is even")
    else:
        print("The number is odd ",)
    print(" Lets start the game!")
    time.sleep(1)
    print("Go ahead guess")
def game():
    global guessesTaken
    guessesTaken=0
    while guessesTaken<6:
        enter=input("Guess:")
        try:
            guess=int(enter)
            if guess>=1 or guess<=100:
                guessesTaken=guessesTaken+1
                if guess>x:
                    print("Your guess is too high")
                if guess<x:
                    print("Your guess is too low")
                if guess==x:
                    break
                
            if guess<1 or guess>100:
                print("Dont be a silly goose!The number is out of range")
                time.sleep(1)
                print("Guess a number between 1 and 100")
        except:
            print("I dont think this is a number")
    if guess==x:
        guessesTaken=str(guessesTaken)
        print("Good job, "+name+"! You guessed my number in "+guessesTaken+" guesses!")
    if guess!=x:
        x=str(x)
        print("Nope. The number I was thinking of was "+x)
playagain="yes"
while playagain=="yes" or playagain=="y" or playagain=="Yes":
    intro()
    game()
    print("Do you want to play again? (yes or no)")
playagain=input()


