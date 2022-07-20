import csv
from itertools import count
import os 

# Assign a variable for the file to load and the path
    ## direct path-> file_to_load = 'Resources\election_results.csv'
#indicrect path (don't know where folder is)
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0 

#Candidate Options and candidate votes 
candidate_options = []

#Declare the empty dictionary 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read to file
with open(file_to_load) as election_data:

    # Read the file with the reader function
    file_reader = csv.reader(election_data)

    #read the header row. 
    headers = next(file_reader)
    

    #Print each row in the CSV file
    for row in file_reader:
        #Add to the total vote count
        total_votes +=1

        #print the candidate name from each row
        candidate_name = row[2]
        
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            
            #Add candidate name to the list of candidates. 
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0 

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

#Save the reults to out text file. 
# using the open() function with the "w" mode we will write data to the txt file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            
        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
            
        #Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
        
        
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

        #print to terminal 
        #print(election_results, end="")
        #print(candidate_results)
        # Save the final vote count to the text file.
        #txt_file.write(election_results)
    txt_file.write(winning_candidate_summary)
    
    #Print the total number of votes
    #print(total_votes)
    #Print the candidate list 
    #print(candidate_votes)

    # #to do: read and anylaze data
    #print each row in the CSV file. 
    #for row in file_reader:
    #    print(row)

 

# Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
    # Write some data to the file.
    #txt_file.write("Hello World")
    # Write three counties to the file.
    # txt_file.write("Arapahoe, " )
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")
    # txt_file.write("Counties in the Election\n--------------------------\nArapahoe\nDenver\nJefferson")




#to do: perform the following analysis 
    
#The data we need to produce
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5.The winner of the election based on popular vote

