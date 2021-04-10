# importing packages


import os
import csv

# loading in csv file
electionData = os.path.join("election_data.csv")
# list for the names of electees
electees = []
# counter for how many votes for each electee based on index in electees list
voteCounter = []
# list that calculates the percentages of votes for each candidadte
votePercentages = []
# counter that registers the total amount of votes
voteTotal = 0

with open(electionData, newline = "") as csvfile:
        csvread = csv.reader(csvfile, delimiter = ",")
        header = next(csvread)
        for row in csvread:
        # adds +1 to vote total
            voteTotal += 1 
        # if clause that adds the electee to electee list if they havent appeared yet
            if row[2] not in electees:
                electees.append(row[2])
                index = electees.index(row[2])
                voteCounter.append(1)
        # else clause that adds a vote to electee if already in list
            else:
                index = electees.index(row[2])
                voteCounter[index] += 1
    
    # for statement looping through each of the votenumbers in voteCounter list that calculates the percentage for each of the candidates
        for voteNumber in voteCounter:
            percentage = (voteNumber / voteTotal) * 100
        # rounds percentage so that it's not too big of a number
            percentage = round(percentage)
        #formats percentage
            percentage = "%.3f%%" % percentage
        # appends percentages to votePercentages list
            votePercentages.append(percentage)
    
    # find index of highest vote count in vote counter list
        highestVoteIndex = voteCounter.index(max(voteCounter))
    # stores the winner in winner variable
        winner = electees[highestVoteIndex]

#statements to print to the console
        print("Election Results")
        print("------------------------------")
        print(f"Total Votes: {str(voteTotal)}")
        print("------------------------------")
        for i in range(len(electees)):
            print(f"{electees[i]}: {str(votePercentages[i]) } ({str(voteCounter[i])})")
        print("------------------------------")
        print(f"Winner: {winner}")
        print("------------------------------")

#will output the program to a text file
with open("output.txt", "w") as x: 
   print("Election Results \n", file = x)
   print("------------------------------\n", file=x)
   print(str(f'Total Votes: {str(voteTotal)}\n'), file = x)
   print("------------------------------\n", file = x)
   for i in range(len(electees)):
        print(str(f'{electees[i]}: {str(votePercentages[i])} ({str(voteCounter[i])})'), file = x)
   print("------------------------------\n", file = x)
   print(str(f'Winner: {winner}\n'), file = x)
   print("------------------------------\n", file = x)
   
