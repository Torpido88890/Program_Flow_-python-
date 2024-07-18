#we can also use break in while loop
available_exit = ["North","East","West","South"]

chosen_exit = ""

while chosen_exit  not in available_exit :
    chosen_exit = input("Please enter your prefered exit direction :")
    if chosen_exit.casefold() == "quit": #Here we used casefold() to take input in any case upper/lower
        print("Game over")
        break
print("----------------------We are glad you just got out from the Hell-----------------------")
