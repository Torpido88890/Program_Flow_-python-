name = input("Please Enter your name: ")
age = int(input("Please Enter your Age: "))

if 18 <= age < 31:
    print("WELCOME TO THE HOLIDAY,{0} ,HAVE A NICE TIME .".format(name))
else:
    print("SORRY BUT YOU ARE NOT ALLOWED , HAVE A NICE TIME ,{0}".format(name))
