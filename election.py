import csv
import os
import statistics
import numpy as np

vote_count = []
candidates = []


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

print(max(vote_count))





    

