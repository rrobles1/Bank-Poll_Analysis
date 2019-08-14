import os
import csv
file = os.path.join("..", "election_data.csv")
file
Results = {}
total_votes = 0

with open(file, 'r') as infile:
    csv_reader = csv.reader(infile)

    next(csv_reader, None)
    
    for row in csv_reader:
        total_votes = total_votes + 1
        if row[2] in Results.keys():
            Results[row[2]] = Results[row[2]] + 1
        else:
            Results[row[2]] = 1

Candidates = []
Votes_won = []

for key, value in Results.items():
    Candidates.append(key)
    Votes_won.append(value)
Percent_won = []
for n in Votes_won:
    Percent_won.append(round(n/total_votes*100, 1))
Final_percent = list(zip(Candidates, Votes_won, Percent_won))

winners = []
for name in Final_percent:
    if max(Votes_won) == name[1]:
        winners.append(name[0])
Winner = winners[0]
Results
Votes_won
Final_percent
Winner