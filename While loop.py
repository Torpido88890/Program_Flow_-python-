#while loop with iterate the code until the condition is True.........
#We can use while loop when we dont know how many times the loop is gonna iterate.....
i=1
while i<11:
    print("The i is now = {} ".format(i))
    i += 1
print("--------------------------------------")

available_exit = ["North","East","West","South"]

chosen_exit = ""

while chosen_exit  not in available_exit :
    chosen_exit = input("Please enter your prefered exit direction :")
print("----------------------We are glad you just got out from the Hell-----------------------")
