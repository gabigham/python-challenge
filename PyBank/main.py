# code for PyBank main part of HW3
# written by George Bigham 7/1/19

import csv
import os

# path to dataset
budget_csv_path = os.path.join('.', 'Resources', 'budget_data.csv')

# variables for output data

changes = []
greatest_inc = 0.0
greatest_dec = 0.0
g_inc_date = ""
g_dec_date = ""


# read file to gather data for analysis
with open(budget_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    for row in csvreader:
        changes.append(float(row[1]))
        
        if float(row[1]) > greatest_inc:
            greatest_inc = float(row[1])
            g_inc_date   = row[0]
        if float(row[1]) < greatest_dec:
            greatest_dec = float(row[1])
            g_dec_date   = row[0]
            

# Write analysis summary file
with open("financial_analysis.txt", "w") as text_file:
    print("Financial Analysis", file = text_file)
    print("-----------------------------", file = text_file)
    print(f"Total Months: {len(changes)}", file = text_file) 
    print(f"Total: ${int(sum(changes))}", file = text_file)
    print(f"Average Change: ${round(sum(changes)/len(changes), 2)}", file = text_file)
    print(f"Greatest Increase in Profits: {g_inc_date} ${greatest_inc}", file = text_file)
    print(f"Greatest Decrease in Profits: {g_dec_date} ${greatest_dec}", file = text_file)
    

with open('test.txt', 'r') as text:
    print(text.read())
    
    
