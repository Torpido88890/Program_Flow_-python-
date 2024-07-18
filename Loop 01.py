"""Stepping through a For Loop:- in this case we should examine
each character in the number string,to check if it's a digit or not."""
number = input("Please enter a number with separators : ")
separators = ""
for i in number:
    if not i.isdigit():
       separators = separators +i
print(separators)

value = "".join(char if char not in separators else " " for char in number ).split()
print(sum([int(val) for val in value ]))
