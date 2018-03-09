import csv
import os
csvpath = os.path.join('budget_data_1.csv')
months = []
revenue = []
sum = 1
revenue = 0

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    #  Each row is read as a row
    for row in csvreader:
        
        print(row)
        months.append(row[0])
        revenue = revenue + int(row[1])


print (months)   

for i in months:
    print (i)
    sum = months.index(i) + 1
   

print (sum)
print (revenue)