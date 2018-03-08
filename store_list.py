import os
import csv

store_csv = os.path.join(‘Resources’, ‘store_items.csv’)
items = {}

with open(store_csv, ‘r’) as csvfile:
   # Split the data on commas
   csvreader = csv.reader(csvfile, delimiter=‘,’)
   for row in csvreader:
       items[row[0]] = row[1]
       print(items)
choice = input(“Would you like to (a)dd a new item, (r)emove an existing one, or to (d)isplay all the items in stock?“)

if (choice == “a”):
   user_input=input(“what do you want to add?“)
   input_number = int(input(“how many” + user_input + “you want to add?“))
   items[user_input] = input_number
   print (items)
elif (choice == “r”):
   user_input=input(“what do you want to remove?“)
   del items[user_input]
   print (items)
elif (choice == “r”):
   print (items)