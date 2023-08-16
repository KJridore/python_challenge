import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join ('.','Resources', 'budget_data.csv')
# budget_csv="ChallengesFolderCamp/python_challenge/PyBank/Resources/budget_data.csv"
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what state they would like to search for
    count=0
    s=0
    Changelist= []
    Monthlist=[]
    previous=0
    # Loop through the data
    for row in csvreader:
        #print(row [0])
        count=count+1
        month=(row[0])
        # print(row)
        s=s+ int(row[1])
        Changelist.append(int(row[1])-previous)
        Monthlist.append(month)
        previous=int(row[1])
        # If the state's name in a row is equal to that which the user input, run the 'print_percentages()' function
        #  if state_to_check == row[0]:
            # print_percentages(row)
    print('Financial Analysis\n------------------------\n')
    print(f'Total Months: {count}')

    print(f'Total: ${s}')
   
    Changelist.pop(0)
    Monthlist.pop(0)
    average=sum(Changelist) / len(Changelist)
    caverage="{:,.2f}".format(average)
    print(f'Average Change: ${caverage}')

#print(min(Changelist))
maxindex=Changelist.index(max(Changelist))
maxdate=Monthlist[maxindex]
print(f'Greatest Increase in Profits: {maxdate} (${max(Changelist)})')

minindex=Changelist.index(min(Changelist))
mindate=Monthlist[minindex]
print(f'Greatest Decrease in Profits: {mindate} (${min(Changelist)})')

# Specify the file to write to
output_path = os.path.join(".", "analysis", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write('Financial Analysis\n------------------------\n')
    txtfile.write(f'Total Months: {count}\n')

    txtfile.write(f'Total: ${s}\n')
    txtfile.write(f'Average Change: ${caverage}\n')
    txtfile.write(f'Greatest Increase in Profits: {maxdate} (${max(Changelist)})\n')
    txtfile.write(f'Greatest Decrease in Profits: {mindate} (${min(Changelist)})\n')

