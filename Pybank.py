import csv
import os
import statistics

csvpath = os.path.join('budget_data_1.csv')
months = []
revenue = []
sum = 1
revenue = 0
test ={}
count1 = 0
value1 = 0
value2 = 0
avgchange = []

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    

    #  Each row is read as a row
    for row in csvreader:
        
        months.append(row[1])
        revenue = revenue + int(row[1])
      
avgchange = [(a + b) / 2 for a, b in zip(months[::2], months[1::2]] 
  
print (avgchange)
print (len(months))
print (sum)
print(revenue/len(months))
print (revenue)
