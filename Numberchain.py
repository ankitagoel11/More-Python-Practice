
choice = "y"
list = []

while choice == "y":

    length_list = int(input("which numebr do you want to add to the list"))
       
    for row in range(length_list):
        list.append(length_list)
        print(row)
    
    choice = input("do you want to continue? ")