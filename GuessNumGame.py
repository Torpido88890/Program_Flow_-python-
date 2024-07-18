# Use of block as if, elif,else

answer = 5
print("Enter any Number between 1 and 10 : ")

guess= int(input())

if guess < answer:
    print("Please guess higher .")
    guess= int(input())
    if guess == answer:
        print("You guessed it correct .")
    else:
        print("Sorry you guessed it incorrect")
elif guess > answer:
    print("Please guess lower .")
    guess= int(input())
    if guess == answer:
        print("You guessed it correct .")
    else:
        print("Sorry you guessed it incorrect")
else:
    print("Hurray!! You guessed it right in the first attempt . ")
