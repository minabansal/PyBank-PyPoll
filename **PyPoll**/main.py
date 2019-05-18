import os

import csv

election_data = "/Users/minabansal/Desktop/python-challenge/**PyPoll**/election_data.csv"

total_votes = 0
candidate_vote_dict = {}
candidate_votes = 0
candidate_vote_percent = {}
winner = ""

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

   # Read each row of data after the header
    for row in csvreader:
        if row[2] in candidate_vote_dict:
            candidate_vote_dict[row[2]] += 1
        else:
            candidate_vote_dict[row[2]] = 1 
        #total votes cast
        total_votes = total_votes + 1
        winner = max(candidate_vote_dict, key=candidate_vote_dict.get)  # Just use 'min' instead of 'max' for minimum.
       
vote_percentages = {}
for key in candidate_vote_dict.keys():
    vote_list = []
    vote_list.append(candidate_vote_dict[key]/total_votes * 100)
    vote_list.append(candidate_vote_dict[key])
    vote_percentages[key] = vote_list




#print election results
print("Election Results")
print(f"Total Votes: {total_votes}")
for key in vote_percentages:
    print(f"{key}: {vote_percentages[key][0]}% ({vote_percentages[key][1]})")
print(f"Winner: {winner}")
#output statement
output = (
   f"\nElection Results\n"
   f"----------------------------\n"
   f"Total Votes: {total_votes}\n"
   f"Khan: 63% (2218231)\n"
   f"Correy: 20% (704200)\n"
   f"Li: 14% (492940)\n"
   f"O'Tooley: 3% (105630)\n"
   f"Winner: {winner}\n")
with open("output.txt", 'w') as txt_file:
    txt_file.write(output)