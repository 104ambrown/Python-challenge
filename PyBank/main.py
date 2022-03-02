# First we need to import dependencies
from datetime import datetime
import os
import csv

# Next we need to establish the path
csvpath = os.path.join("C:/Users/abrow/Desktop/EMERSON_BOOTCAMP/BOOTCAMP_AMB/Homeworks/Python-challenge/PyBank/Resources/budget_data.csv")

# Creating lists to store data in and defining variables
months = []
profitLosses = []

# reading the csv file into VS Code
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # reading each row of data into the script
    for row in csvreader:
        months.append(row[0])
        profitLosses.append(int(row[1]))

    # counting how many months are in the dataset
    numMonths = len(months)

    # setting the variables 
    x = 1
    y = 0

    # making a place holder to calculate change month-to-month
    avgChange = (profitLosses[1]-profitLosses[0])

    # list to hold the month-to-month change
    monthlyChanges = []

    # interating through dataset to calculate the monthly changes
    for month in range(numMonths-1):
        avgChange = (profitLosses[x]-profitLosses[y])
        monthlyChanges.append(int(avgChange))
        x = x + 1
        y = y + 1

    # Using the calculations generated above to find the average for the whole dataset
    # rounding to 2 decimals for cents
    avgMonthlyChange = round(sum(monthlyChanges)/(numMonths-1),2)

    # finding the greatest profit and losses
    greatestProfit = max(monthlyChanges)
    greatestLoss = min(monthlyChanges)

    # indexing by the changes to find the dates on which they occured
    profitIndex = monthlyChanges.index(greatestProfit)
    lossIndex = monthlyChanges.index(greatestLoss)

    # Getting the months
    greatestProfitMonth = months[profitIndex + 1]
    greatestLossMonth = months[lossIndex + 1]

 # Printing the values to the console
print("PyBank Financial Analysis")
print("------------------------------------------")
print(f"Number of months in the dataset: {numMonths}")
print(f"Total Profits/Losses for the period: ${sum(profitLosses)}")
print(f"Average monthly change: ${avgMonthlyChange}")
print(f"The greatest increase in profits was: ${greatestProfit} in {greatestProfitMonth}")
print(f"The greatest loss in profits was: ${greatestLoss} in {greatestLossMonth}")

# Writing the output to a text file

output_path = os.path.join("C:/Users/abrow/Desktop/EMERSON_BOOTCAMP/BOOTCAMP_AMB/Homeworks/Python-challenge/PyBank/Analysis/pybank_financial_analysis.txt")

with open(output_path, "w") as fin_analysis:
    fin_analysis.write("PyBank Financial Analysis\n")
    fin_analysis.write("------------------------------------------\n")
    fin_analysis.write(f"Number of months in the dataset: {numMonths}\n")
    fin_analysis.write(f"Total Profits/Losses for the period: ${sum(profitLosses)}\n")
    fin_analysis.write(f"Average monthly change: {avgMonthlyChange}\n")
    fin_analysis.write(f"The reatest increase in profits was: {greatestProfit} in {greatestProfitMonth}\n")
    fin_analysis.write(f"The greatest loss in profits was: {greatestLoss} in {greatestLossMonth}\n")

    fin_analysis.close()

