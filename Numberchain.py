
choice = "y"
list = []

while choice == "y":

    length_list = int(input("which numebr do you want to add to the list"))
    list.append(length_list)
    for row in list:
        print(row)
    choice = input("do you want to continue? ")