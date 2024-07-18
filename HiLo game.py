low = 1
high = 1000

print("Please think of a number between {0} and {1}".format(low,high))
input("Please ENTER to start")

guesses= 1
while True:
    print("\t Guessing in the range between {} and {}".format(low ,high))
    guess = low + (high - low)//2
    high_low = input("My guess is {} . Should I guess higher or lower "
                     "Enter h,l or c if my answer was correct ."
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess +1
    elif high_low == "l":
        high = guess -1
    elif high_low == "c" :
        print("I got it in {} guesses !".format(guesses))
        break
    else:
        print("Please enter h,l or c")

    guesses += 1   # this is an augmented assignment which is used to save work ,since it makes a variable and modifies it instead of destroying and creating it again.
