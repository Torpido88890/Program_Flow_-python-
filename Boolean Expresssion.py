day = "Monday"
temperature = 30
rain = True

if day == "Saturday" and temperature > 27 and not rain:
    print("1.GO SWIMMING ")

else:
    print(" 1.Learn Python ")
#here since we have used and opearator then this code will never print the if condition since rain is always true bt the operator is for not and....

#on contrary the code wrtten below can print the if condition since the operator used is not or ..
if day == "Monday" and temperature > 27 or not rain:
    print("2.GO SWIMMING ")

else:
    print("2.Learn Python ")
