import os
import csv


vote_csv_path = "Resources/election_data.csv"

# variable and dictionary for vote counts
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0


# read and agragate votes for candidates
with open(vote_csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # remove header
    next(csvreader)

    for row in csvreader:
        total_votes += 1
        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1


# find winner
for key, value in candidates.items():
    if value > winner_votes:
        winner = key
        winner_votes = value


# write results to election_results.txt
with open("election_results.txt", "w") as text_file:
    print("Election Results", file = text_file)
    print("-----------------------------", file = text_file)
    print(f"Total Votes: {total_votes}", file = text_file)
    print("-----------------------------", file = text_file)
    for key, value in candidates.items():
        print(key + ": " + str( "%.2f%%" % ((value/total_votes)%100)) + " (" + str(value) + ")", file = text_file)
    print("-----------------------------", file = text_file)        
    print("Winner: " + winner, file = text_file)
    print("-----------------------------", file = text_file)    


# Display summary in command line
with open('election_results.txt', 'r') as text:
    print(text.read())

