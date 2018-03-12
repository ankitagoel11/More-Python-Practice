import csv
import os
import statistics
import numpy as np

vote_count = []
candidates = []
i=0
vote_percent =[]

csvpath = os.path.join('election_data_1.csv')

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)
    for row in csvreader:
        candidates.append(row[2])

    print(len(candidates))
    myset = set(candidates)
    my_new_list = list(myset)
    print (myset)
 
for x in my_new_list:
    vote_count.append(candidates.count(x))

for y in vote_count:
    vote_percent.append((y*100)/len(candidates))

print(vote_percent)

print(max(vote_count))

print ("Election Results")
print ("..................................")
print ("Total Votes: " + str(len(candidates)))
print ("..................................")
for x in my_new_list:
    print( x + ":" + str(vote_percent[i]) + "%  (" + str(vote_count[i]) + ")"  )
    i += 1

print ("..................................")

    

