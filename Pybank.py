import csv
import os
csvpath = os.path.join('budget_data_1.csv')
months = []
sum=1

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    
    #  Each row is read as a row
    for row in csvreader:
        
        print(row)
        months.append(row[0])

print (months)   

for i in months:
    print (i)
    sum = months.index(i)

print (sum)