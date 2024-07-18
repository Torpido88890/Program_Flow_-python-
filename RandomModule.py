#Random module has randint(a,b) function that generate random integer between the given range(a,b)
import random

highest = 10
answer = random.randint(1,highest)
print("Enter any Number between 1 and {} : ".format(highest))

guess= int(input())

if guess == answer:
    print("You guessed it correct in the first attempt .")
else:
    if guess < answer:
       print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done ,you guessed it right .")

    else:
        print("Sorry ,you haven't guessed it correct.")
