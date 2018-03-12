import csv
import os
import statistics
import numpy as np


# Defining the variables and lists
vote_count = []
candidates = []
i=0
j=0
vote_percent =[]

#syntax to open csv
csvpath = os.path.join('election_data_1.csv')

with open(csvpath, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Making a list with all the votes for each candidate
    next(csvreader)
    for row in csvreader:
        candidates.append(row[2])

  
    # calculation of unque candidates and putting them in a list
    myset = set(candidates)
    my_new_list = list(myset)

#Count of vaotes for each candidate is stored in a list named vote_count

for x in my_new_list:
    vote_count.append(candidates.count(x))

#Calculate vote percent of each candidate and store it in a list called vote_percent

for y in vote_count:
    vote_percent.append((y*100)/len(candidates))

# Determine the winner
winner = candidates[vote_count.index(max(vote_count))]

#Print statements to display desired parameters
print ("Election Results")
print ("..................................")
print ("Total Votes: " + str(len(candidates)))
print ("..................................")
for x in my_new_list:
    print( x + ":" + str(vote_percent[i]) + "%  (" + str(vote_count[i]) + ")"  )
    i += 1

print ("..................................")
print ("Winner : " + winner)

with open("results1.txt", "w") as text_file:
    print ("Election Results", file = text_file)
    print ("..................................", file = text_file)
    print ("Total Votes: " + str(len(candidates)), file = text_file)
    print ("..................................", file = text_file)
    for x in my_new_list:
        print ( x + ":" + str(vote_percent[j]) + "%  (" + str(vote_count[j]) + ")", file = text_file)
        j += 1

    print ("..................................", file = text_file )
    print ("Winner : " + winner, file = text_file)
    

