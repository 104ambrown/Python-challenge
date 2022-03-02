#Py Poll main.py
# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 
# Your task is to create a Python script that analyzes the votes and calculates each of the following:

# Importing the os and csv reading modules
import os
import csv

csvpath = os.path.join("PyPoll/Resources/election_data.csv")

# Creating lists to stare the data in

count = 0
candidateList = []
kahnVotes = 0
correyVotes = 0
liVotes = 0
otooleyVotes = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # reading in each row of data after the header
    for row in csvreader:

        # Count all the votes
        count = count + 1
        
        # List the candidates
        if row[2] not in candidateList:
          candidateList.append(row[2])

        if row[2] == candidateList[0]:
          kahnVotes = kahnVotes + 1

        elif row[2] == candidateList[1]:
          correyVotes = correyVotes + 1

        elif row[2] == candidateList[2]:
          liVotes = liVotes + 1
        
        elif row[2] == candidateList[3]:
          otooleyVotes = otooleyVotes + 1
  
# Calculating percentage of votes for each candidate

kahnPercentage = ("%.2f" % ((kahnVotes/count)*100))
correyPercentage = ("%.2f" % ((correyVotes/count)*100))
liPercentage = ("%.2f" % ((liVotes/count)*100))
otooleyPercentage = ("%.2f" % ((otooleyVotes/count)*100))

if max(kahnVotes, correyVotes, liVotes, otooleyVotes) == kahnVotes:
  winner = "Kahn"

elif max(kahnVotes, correyVotes, liVotes, otooleyVotes) == correyVotes:
  winner = "Correy"

elif max(kahnVotes, correyVotes, liVotes, otooleyVotes) == liVotes:
  winner = "Li"

else:
  winner = "O'Tooley"

# Printing final results to terminal

print ("Election Results")
print ("-------------------------------------")
print (f"Total votes cast: {count}")
print ("-------------------------------------")
print (f"Votes for Kahn: {kahnVotes}, or {kahnPercentage}% of the votes")
print (f"Votes for Correy: {correyVotes}, or {correyPercentage}% of the votes")
print (f"Votes for Li: {liVotes}, or {liPercentage}% of the votes")
print (f"Votes for O'Tooley: {otooleyVotes}, or {otooleyPercentage}% of the votes")
print ("-------------------------------------")
print (f"Winner: {winner}")
print ("-------------------------------------")

# Writing results to a text file

output_path = os.path.join("PyPoll/Analysis/pypoll_results.txt")

with open(output_path, "w") as file:

  file.write("Election Results")
  file.write("-------------------------------------")
  file.write(f"Total votes cast: {count}")
  file.write("-------------------------------------")
  file.write(f"Votes for Kahn: {kahnVotes}, or {kahnPercentage}% of the votes")
  file.write(f"Votes for Correy: {correyVotes}, or {correyPercentage}% of the votes")
  file.write(f"Votes for Li: {liVotes}, or {liPercentage}% of the votes")
  file.write(f"Votes for O'Tooley: {otooleyVotes}, or {otooleyPercentage}% of the votes")
  file.write("-------------------------------------")
  file.write(f"Winner: {winner}")
  file.write("-------------------------------------")