import csv
import os
import statistics
import numpy

#defining variables and lists
months = []
revenue = []
date =[]
revenue = 0
avg_change = []
test ={}
count1 = 0
value1 = 0
value2 = 0
i=0
csvpath = os.path.join('budget_data_1.csv')

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    

    #  Each row is read as a row and monthly revenue values are stored in months list
    for row in csvreader:
        date.append(row[0])
        months.append(row[1])
        revenue = revenue + int(row[1])
   
    #calculating change in every month and saving it to the avg_change list
    while i<len(months) - 1:
        value1 = months[i]
        value2 = months[i+1]
        avgchange = (int(value2) - int(value1))
        avg_change.append(avgchange)
        i = i+1
        
s = avg_change.index(max(avg_change)) # extracting index to get corresponding dat value
t = avg_change.index(min(avg_change)) # extracting index to get corresponding dat value
r = numpy.mean(avg_change)            #taking average of the change


print (" Financial Analysis")
print ("..........................")
print ("Total number of months :" + str(len(months)))
print ("Total Revenue : $" + str(revenue))
print ("Averge Revenue Change: $" + str(r))
print ("Greatest increase in Revenue: " + str(date[s+1]) + " ($" + str(max(avg_change)) + ")")
print ("Greatest decrease in Revenue: " + str(date[t+1]) + " ($" + str(min(avg_change)) + ")")

with open("results_pybank.txt", "w") as text_file:
    print (" Financial Analysis", file = text_file)
    print ("..........................", file = text_file)
    print ("Total number of months :" + str(len(months)), file = text_file)
    print ("Total Revenue : $" + str(revenue), file = text_file)
    print ("Averge Revenue Change: $" + str(r), file = text_file)
    print ("Greatest increase in Revenue: " + str(date[s+1]) + " ($" + str(max(avg_change)) + ")", file = text_file)
    print ("Greatest decrease in Revenue: " + str(date[t+1]) + " ($" + str(min(avg_change)) + ")", file = text_file)