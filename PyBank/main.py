# First we need to import the csv file of our data
import os

import csv

# Next we need to establish the path
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# I think we need to define variables here? Maybe? Or maybe we creates lists to store the data, is there a difference?
Date = {0}
"Profit/Losses" = {1}
#I think I just created 2 dictionaries and told them what col

# open the file, read it, write it, do something to it *le shrug*
with open(budget_data.csv) as csvfile:
    csvreader - csv.reader(csvfile, delimiter=",")
    for row in csvreader
        # Add Date
        Date.append(row[0])
        # Add Profit/Losses
        Profit_Losses.append(row[1])

with open(budget_data, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Date", "Profits/Losses"])


# Count the things, and by things, I mean the number of months in the data set
   def months(Date):
       print(f"The number of months in the data set are...")
       for value in months
            print(value)
        print("After ", + len(Date) + " long months at sea I finally made landfall on the southern shores of the dataset")


# Calculate the net gain or loss over the period
    # Find the first value in the gain or loss column
    # Find the last value in the gain or loss column 
    # calculate using those values the net gain or loss
        # or I guess we could just use a simple sum command, screw you VBA you high maintenance asshole


#Calculate the average of changes in "Profit/Losses" over the time period
    

# Greatest increase in profits,
    # Use a while loop to look for greatest value
    # Print greatest value
    # Print date it occured
    # Print amount
    maximum = max{"Profit/Losses"}
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