import csv
import os
import statistics
import numpy

csvpath = os.path.join('budget_data_1.csv')
months = []
revenue = []
revenue = 0
avg_change = []
test ={}
count1 = 0
value1 = 0
value2 = 0
i=0

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    

    #  Each row is read as a row
    for row in csvreader:
        
        months.append(row[1])
        revenue = revenue + int(row[1])
   

    while i<len(months) - 1:
        value1 = months[i]
        value2 = months[i+1]
        avgchange = ((int(value1) - int(value2))/int(value1))*100 
        avg_change.append(avgchange)
        i = i+1
       


print(avgchange)
print (len(months))
print(revenue/len(months))
print (revenue)
print (max(avg_change))