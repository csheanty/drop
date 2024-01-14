#Guess the number using import random
import random


def myFunc():
    guess = 0
    num = random.randint(1,20)

    while guess != num:
        guess = int(input("Guess the number: "))
        if guess < num:
             print("Too low")
        elif guess > num:
             print("Too high")

    print("You've guessed the right number!")


def myComp(x):

    guess = 0
    high = x
    low = 0
    resp = ""

    while resp != "c":
        print(guess)
        resp = input("HIGH - h? LOW - l? CORRECT - c?")

        if resp == "h":
            high = guess - 1
            guess = random.randint(low,high)

        elif resp == "l":
            low = guess + 1
            guess = random.randint(low,high)

    print("Congrats")

myComp(15)

