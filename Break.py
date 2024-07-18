# we use Break to skip the lines of code by applying it exactly before the part that have to be skipped.
shopping_list = ["curd","milk","sugar","spam","pen"]
item_find = input("Enter the item to find from the shopping list :")
found_at = None

for index in range(len(shopping_list)):
    if shopping_list[index] == item_find:
        found_at = index
        break
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_find.title()))
