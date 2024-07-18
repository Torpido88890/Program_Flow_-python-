# we use continue to skip the lines of code by aplying it exactly before the line that have to be skipped.
shopping_list = ["curd","milk","sugar","spam","pen"]
for i in shopping_list:
    if i == "spam":
        continue
    print("Buy {}".format(i))
