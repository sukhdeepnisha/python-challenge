import os
import csv
# path for csv file
csv_path = os.path.join('..', 'PyPoll\Resources','election_data.csv')
# path for output txt file
output_file_path=os.path.join('..', 'PyPoll\Analysis','output.txt')
# declaring dictionary for saving candidate name as key and number of votes as value
candidate_dict={}

total_votes=0

# reading using CSV 
with open(csv_path) as csv_file:

    # CSV reader specifies delimeter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # read the header row first (skip if there is no header)
    csv_header = next(csv_reader)
    
    
    for row in csv_reader:
        ballot_id = row[0]
        county = row[1]
        candidate = row[2]
        
        # counting total votes
        total_votes = total_votes + 1
        
        # if key (candidate name) is present then increasing the number of votes by 1
        if candidate in candidate_dict:
            # getting the value which is number of votes
            currrent_count=candidate_dict.get(candidate)
            # increasing number of votes by 1
            candidate_dict[candidate]=currrent_count+1
        else:
            # if candidate is not added in the dict then adding 
            # candidate name as key and setting value as 1
            candidate_dict[candidate]=1

# writing to the output file along with printing on the screen
with open(output_file_path,"w") as file:
    
    file.write("Election Results\n")
    print("Election Results")

    file.write("----------------------------\n")
    print("----------------------------")

    file.write("Total Votes: "+str(total_votes)+"\n")
    print("Total Votes: "+str(total_votes))

    file.write("----------------------------\n")
    print("----------------------------")

    # variable to find out the max votes
    max_votes=0

    # iterating over the dict
    for key in candidate_dict:

        # finding the percentage and printing it
        file.write(key+": "+ str(round((candidate_dict.get(key)/total_votes)*100,3)) +"% ("+ str(candidate_dict.get(key))+")\n" )
        print(key+": "+ str(round((candidate_dict.get(key)/total_votes)*100,3)) +"% ("+ str(candidate_dict.get(key))+")" )
        
        #finding out the max votes and winner
        if(max_votes < candidate_dict.get(key)):
            max_votes= candidate_dict.get(key)
            winner=key


    file.write("----------------------------\n")
    print("----------------------------")

    file.write("Winner: "+winner+"\n")
    print("Winner: "+winner)

    file.write("----------------------------\n")
    print("----------------------------")







    
      