# step 1: import csv files
# step 2: loop through csv and count rows for total months
# step 3: count rows for profit/loss
# step 4: find averages: add csv values to list and then Average(list) 
import os
import csv
csv_path = os.path.join("..", "PyBank", "budget_data.csv")
csv_path
with open(csv_path, "r") as infile:
    csv_reader = csv.reader(infile, delimiter = ",")
    print(next(csv_reader))
    changes = []
previous_profit = 0
with open(csv_path, "r") as infile:
    csv_reader = csv.reader(infile, delimiter = ",")
    print(next(csv_reader))
#     print_totals(budget_data)
    for row in csv_reader:
        current_profit = row[1]
        change = int(current_profit) - int(previous_profit)
        changes.append(change)
        previous_profit = current_profit
    changes = changes[1:]
    max_profit = max(changes)
    max_loss = min(changes)
Avg_Profit_Losses = sum(changes) / len(changes)