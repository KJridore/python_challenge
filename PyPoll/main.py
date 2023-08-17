import os
import csv

election_csv = os.path.join ('.','Resources', 'election_data.csv')
# budget_csv="ChallengesFolderCamp/python_challenge/PyBank/Resources/budget_data.csv"
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    # Prompt the user for what state they would like to search for
    Totalvote= 0
    Candidates= []
    candidateVoteCount= {}
    candidateVotePercentage={}

    # Loop through the data
    for row in csvreader:
        #print(row)
        Totalvote=Totalvote+1
        C=row[2]
        if C not in Candidates:
            Candidates.append(C)
            candidateVoteCount[C]=0
        candidateVoteCount[C]+=1
    # Loop to iterate over candidates dictionary 
    # : colon, ; semicolon, _ underscore, ' single quote, " double"
    for candidate,vote in candidateVoteCount.items():
        candidatesPercentage= (vote/Totalvote)* 100
        candidateVotePercentage[candidate]=candidatesPercentage

    print('Election Results\n------------------------\n')
    print(f'Total Votes: {Totalvote}')
    print('\n------------------------\n')
    for candidate,percentage in candidateVotePercentage.items():
        print(f"{candidate}: {percentage:.3f}% ({candidateVoteCount.get(candidate)})")
    print('\n------------------------\n')   
    print('Winner: ',max(candidateVoteCount,key=candidateVoteCount.get))
    print('\n------------------------\n')

    # Specify the file to write to
output_path = os.path.join(".", "analysis", "new.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results\n------------------------\n')
    txtfile.write(f'Total Votes: {Totalvote}\n')

    txtfile.write(f'\n------------------------\n')
    for candidate,percentage in candidateVotePercentage.items():
        txtfile.write(f"{candidate}: {percentage:.3f}% ({candidateVoteCount.get(candidate)})\n")
    txtfile.write(f'\n------------------------\n')
    txtfile.write(f'Winner: {max(candidateVoteCount,key=candidateVoteCount.get)}\n')
    txtfile.write('\n------------------------\n')