# First we need to import the csv file of our data
from datetime import datetime
import os

import csv

# Next we need to establish the path
budget_data = os.path.join('..', 'Resources', 'budget_data.csv')

# Creating lists to store data in
Date = []
profitLosses = []

# defining csvreader
csvreader = csv.reader(budget_data, delimiter=',')

# open the file, read it, write it, do something to it *le shrug*
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
        print(csvreader)
    csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")

    for row in csvreader:
        # Add Date
        Date.append(row[0])
        # Add Profit/Losses
        profitLosses.append(row[1])

# I think we need to define variables here? Maybe? Or maybe we creates lists to store the data, is there a difference?
Date = {0}
profitLosses = {1}

def bank_data(csvpath):
    Date = datetime(csvreader[0])
    profitLosses = int(csvreader[1])




with open(csvpath, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Date", "profitLosses"])


# Count the things, and by things, I mean the number of months in the data set
def months(Date):
       print(f"There are " + len(Date) + " months in the data set.")
       for value in months:
            print(value)
print("After ", + len(Date) + " long months at sea I finally made landfall on the southern shores of the dataset")


# Calculate the net gain or loss over the period
    # Find the first value in the gain or loss column
    # Find the last value in the gain or loss column 
    # calculate using those values the net gain or loss
        # or I guess we could just use a simple sum command, screw you VBA you high maintenance jerk
sum(profitLosses)
length = len(profitLosses)
start = 1
print(sum(range(1)))


#Calculate the average of changes in "Profit/Losses" over the time period
def average(profitLosses):
        length = len(profitLosses)
        total = 0.0
        for number in profitLosses:
            total += profitLosses
        return total / length

print(average(range(1)))

# Greatest increase in profits,
    # Use a while loop to look for greatest value
    # Print greatest value
    # Print date it occured
    # Print amount
maximum = max{profitLosses}
    print(maximum)
    print("I won big betting on ponies and made ", + maximum, + " dollars on ", + Date)

# Greatest decrease in losses
    # Use a while loop to look for lowest value
    # Print lowest value
    # Print date it occured
    # Print amount
minimum = min{"Profit/Losses"}
print(minimum)
print("I hit rock bottom betting on ponies and lost ", + minimum, + "dollars on ", + Date)

# We need to print the analysis to terminal
# Lastly we need to export our analysis as a text file 
# Setting variable for output file
output_file = os.path.join("PyBank_Analysis.txt")

# Open the output file
with open(output_file, "w", newline="") as textfile:
    writer = textfile.writer(textfile)